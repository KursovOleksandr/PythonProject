import xml.etree.ElementTree as ET
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def find_incoming_by_group_number(xml_file, group_number):

    tree = ET.parse(xml_file)
    root = tree.getroot()

    for group in root.findall("group"):
        number = group.find("number")

        if number is not None and number.text == str(group_number):

            incoming = group.find("timingExbytes/incoming")

            if incoming is not None:
                logging.info(f"group {group_number} incoming = {incoming.text}")
                return incoming.text
            else:
                logging.info(f"group {group_number} has no incoming value")
                return None

    logging.info(f"group {group_number} not found")
    return None


find_incoming_by_group_number("groups.xml", 2)