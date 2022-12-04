from collections import defaultdict
import drksql


def nested_dict(n, typ):
    if n == 1:
        return defaultdict(typ)
    else:
        return defaultdict(lambda: nested_dict(n - 1, typ))


def set_std_config():
    local_config = nested_dict(2, str)
    # generate Standard-Config
    local_config['allgemein']['beep'] = "False"
    local_config['allgemein']['debug'] = "False"
    local_config['allgemein']['btn_h_h'] = "3"
    local_config['allgemein']['btn_h_l'] = "2"
    local_config['allgemein']['btn_w_h'] = "8"
    local_config['allgemein']['btn_w_l'] = "6"
    local_config['allgemein']['geometry'] = "480x320"
    local_config['allgemein']['heartbeat'] = "0"
    local_config['allgemein']['kommen_gehen_preset'] = "None"
    local_config['allgemein']['logo_fil'] = "zeiterfassung_logo.png"
    local_config['allgemein']['max_anwesend'] = "0"
    local_config['allgemein']['processid'] = "0"
    local_config['allgemein']['rfid_unbekannt_btf'] = "False"
    local_config['allgemein']['showworktype_btf'] = "True"
    local_config['allgemein']['show_QR'] = "False"
    local_config['allgemein']['standardworktype'] = "1"
    local_config['allgemein']['startbeep'] = "True"
    local_config['allgemein']['timezone'] = "Europe/Berlin"
    local_config['allgemein']['url_web'] = "https://www.drk-hochheim.de"
    local_config['allgemein']['url_zet'] = "https://zeiterfassung.drk-hochheim.de"
    local_config['farben']['bg'] = "#FFFFFF"
    local_config['farben']['bg_er'] = "#e60004"
    local_config['farben']['bg_wt'] = "#FFFF00"
    local_config['farben']['fg'] = "#002d55"
    local_config['farben']['fg_er'] = "#ebc634"
    local_config['farben']['fg_wt'] = "#000000"
    local_config['farben']['ge'] = "#e60004"
    local_config['farben']['ko'] = "#2dff55"
    local_config['texte']['auff_input'] = "Eingabe Bitte!"
    local_config['texte']['ge'] = "Tschüß"
    local_config['texte']['ge_btn'] = "GEHEN"
    local_config['texte']['ko'] = "Willkommen"
    local_config['texte']['ko_btn'] = "KOMMEN"
    local_config['texte']['org'] = "DRK"
    local_config['texte']['rfid_unbekannt'] = "Ausweis unbekannt"
    local_config['texte']['term_name'] = "Tür X"
    local_config['texte']['term_place'] = "intern"
    local_config['texte']['titel'] = "Zeiterfassung"
    local_config['texte']['verein'] = "OV Hochheim a.M. e.V."
    local_config['texte']['worktype_1'] = "9"
    local_config['texte']['worktype_2'] = "6"
    local_config['texte']['worktype_3'] = "5"
    local_config['texte']['worktype_4'] = "7"
    local_config['texte']['worktype_5'] = "8"
    local_config['texte']['worktype_info'] = "Bitte Art der Arbeit wählen:"
    local_config['texte']['worktype_title'] = "Art der Arbeit"
    local_config['allgemein']['wt_btn_h'] = "2"
    local_config['allgemein']['wt_btn_w'] = "2"
    return local_config


def read_configvalue(uuid, option):
    local_config = nested_dict(2, str)
    conn = drksql.open_connection()
    value = ""
    # Get Cursor
    cur = conn.cursor()
    query = "SELECT * FROM ze_terminals WHERE uuid=? AND option=?"
    qvals = (str(uuid), option)
    cur.execute(query, qvals)
    for (row) in cur:
        option = str(row[1])
        opt = option.split("_", 1)
        value = str(row[2])
        local_config[opt[0]][opt[1]] = value
    drksql.close_connection(conn)
    return value


def write_configvalue(guid, option, value, connection=False):
    if not connection:
        try:
            conn = drksql.open_connection()
        except mariadb.Error as e:
            print(e)
    else:
        conn = connection
    query = "INSERT INTO ze_terminals (value, uuid, option) " \
        "VALUES ('"+str(value)+"','"+str(guid)+"','"+str(option)+"') " \
        "ON DUPLICATE KEY UPDATE value='"+str(value)+"';"
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    if not connection:
        drksql.close_connection(conn)
    return True


def check_config(uuid):
    # if config is in DB then TRUE else FALSE
    conn = drksql.open_connection()

    # Get Cursor
    cur = conn.cursor()
    query = "SELECT * FROM ze_terminals WHERE uuid=?"
    qvals = (str(uuid),)
    cur.execute(query, qvals)
    cur.fetchall()
    if cur.rowcount > 1:
        return True
    else:
        return False


def write_config(uuid, config):
    try:
        conn = drksql.open_connection()
        write_configvalue(uuid, 'allgemein_beep', config['allgemein']['beep'], conn)
        write_configvalue(uuid, 'allgemein_debug', config['allgemein']['debug'], conn)
        write_configvalue(uuid, 'allgemein_btn_h_h', config['allgemein']['btn_h_h'], conn)
        write_configvalue(uuid, 'allgemein_btn_h_l', config['allgemein']['btn_h_l'], conn)
        write_configvalue(uuid, 'allgemein_btn_w_h', config['allgemein']['btn_w_h'], conn)
        write_configvalue(uuid, 'allgemein_btn_w_l', config['allgemein']['btn_w_l'], conn)
        write_configvalue(uuid, 'allgemein_geometry', config['allgemein']['geometry'], conn)
        write_configvalue(uuid, 'allgemein_heartbeat', config['allgemein']['heartbeat'], conn)
        write_configvalue(uuid, 'allgemein_kommen_gehen_preset', config['allgemein']['kommen_gehen_preset'], conn)
        write_configvalue(uuid, 'allgemein_logo_fil', config['allgemein']['logo_fil'], conn)
        write_configvalue(uuid, 'allgemein_max_anwesend', config['allgemein']['max_anwesend'], conn)
        write_configvalue(uuid, 'allgemein_processid', config['allgemein']['processid'], conn)
        write_configvalue(uuid, 'allgemein_rfid_unbekannt_btf', config['allgemein']['rfid_unbekannt_btf'], conn)
        write_configvalue(uuid, 'allgemein_showworktype_btf', config['allgemein']['showworktype_btf'], conn)
        write_configvalue(uuid, 'allgemein_show_QR', config['allgemein']['show_QR'], conn)
        write_configvalue(uuid, 'allgemein_standardworktype', config['allgemein']['standardworktype'], conn)
        write_configvalue(uuid, 'allgemein_startbeep', config['allgemein']['startbeep'], conn)
        write_configvalue(uuid, 'allgemein_timezone', config['allgemein']['timezone'], conn)
        write_configvalue(uuid, 'allgemein_url_web', config['allgemein']['url_web'], conn)
        write_configvalue(uuid, 'allgemein_url_zet', config['allgemein']['url_zet'], conn)
        write_configvalue(uuid, 'farben_bg', config['farben']['bg'], conn)
        write_configvalue(uuid, 'farben_bg_er', config['farben']['bg_er'], conn)
        write_configvalue(uuid, 'farben_bg_wt', config['farben']['bg_wt'], conn)
        write_configvalue(uuid, 'farben_fg', config['farben']['fg'], conn)
        write_configvalue(uuid, 'farben_fg_er', config['farben']['fg_er'], conn)
        write_configvalue(uuid, 'farben_fg_wt', config['farben']['fg_wt'], conn)
        write_configvalue(uuid, 'farben_ge', config['farben']['ge'], conn)
        write_configvalue(uuid, 'farben_ko', config['farben']['ko'], conn)
        write_configvalue(uuid, 'texte_auff_input', config['texte']['auff_input'], conn)
        write_configvalue(uuid, 'texte_ge', config['texte']['ge'], conn)
        write_configvalue(uuid, 'texte_ge_btn', config['texte']['ge_btn'], conn)
        write_configvalue(uuid, 'texte_ko', config['texte']['ko'], conn)
        write_configvalue(uuid, 'texte_ko_btn', config['texte']['ko_btn'], conn)
        write_configvalue(uuid, 'texte_org', config['texte']['org'], conn)
        write_configvalue(uuid, 'texte_rfid_unbekannt', config['texte']['rfid_unbekannt'], conn)
        write_configvalue(uuid, 'texte_term_name', config['texte']['term_name'], conn)
        write_configvalue(uuid, 'texte_term_place', config['texte']['term_place'], conn)
        write_configvalue(uuid, 'texte_titel', config['texte']['titel'], conn)
        write_configvalue(uuid, 'texte_verein', config['texte']['verein'], conn)
        write_configvalue(uuid, 'texte_worktype_1', config['texte']['worktype_1'], conn)
        write_configvalue(uuid, 'texte_worktype_2', config['texte']['worktype_2'], conn)
        write_configvalue(uuid, 'texte_worktype_3', config['texte']['worktype_3'], conn)
        write_configvalue(uuid, 'texte_worktype_4', config['texte']['worktype_4'], conn)
        write_configvalue(uuid, 'texte_worktype_5', config['texte']['worktype_5'], conn)
        write_configvalue(uuid, 'texte_worktype_info', config['texte']['worktype_info'], conn)
        write_configvalue(uuid, 'texte_worktype_title', config['texte']['worktype_title'], conn)
        write_configvalue(uuid, 'allgemein_wt_btn_h', config['allgemein']['wt_btn_h'], conn)
        write_configvalue(uuid, 'allgemein_wt_btn_w', config['allgemein']['wt_btn_w'], conn)
        drksql.close_connection(conn)
    except mariadb.Error as e:
        print(e)
    return True


def get_config(uuid):
    local_config = nested_dict(2, str)
    conn = drksql.open_connection()

    # Get Cursor
    cur = conn.cursor()
    query = "SELECT * FROM ze_terminals WHERE uuid=?"
    qvals = (str(uuid),)
    cur.execute(query, qvals)
    for (row) in cur:
        option = str(row[1])
        opt = option.split("_", 1)
        value = str(row[2])
        local_config[opt[0]][opt[1]] = value
    drksql.close_connection(conn)
    return local_config
