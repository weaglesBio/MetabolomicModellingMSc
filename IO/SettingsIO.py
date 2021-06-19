import xml.etree.ElementTree as ET

def load_preferences():
    preferences = []
    try:
            # If errors while attempt to read, requires conversion.
        with open("settings.xml") as f:
            settings_tree_data = f.read()

    except Exception as err:
        print(err)

    settings_root = ET.fromstring(settings_tree_data)

    smooth = settings_root.find("./settings/smooth")
    if smooth is not None:
        preferences.append(("smooth", smooth.text))

    decdp = settings_root.find("./settings/decdp")
    if decdp is not None:
        preferences.append(("decdp", decdp.text))

    return preferences

def load_database_paths():
    
    database_paths = []
    try:
            # If errors while attempt to read, requires conversion.
        with open("settings.xml") as f:
            settings_tree_data = f.read()

    except Exception as err:
        print(err)

    settings_root = ET.fromstring(settings_tree_data)

    for database in settings_root.findall("./settings/databases/database"):
        database_paths.append(database.text)

    return database_paths

def write_settings(settings):

    peakmlviewer_node = ET.Element("peakmlviewer")
    settings_node = ET.SubElement(peakmlviewer_node,"settings")
    ET.SubElement(settings_node,"smooth").text = settings.get_preference_by_name("smooth")
    ET.SubElement(settings_node,"decdp").text = settings.get_preference_by_name("decdp")
    databases_node = ET.SubElement(settings_node,"databases")

    for database_path in settings.get_database_paths(): 
        ET.SubElement(databases_node,"database").text = database_path

    tree = ET.ElementTree(peakmlviewer_node)
    tree.write("settings.xml")
