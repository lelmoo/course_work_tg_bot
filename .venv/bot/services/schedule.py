from bot.services.connection import get_connection, close_connection


def get_schedule(class_number, class_letter):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM get_schedule(%s, %s)", (class_number, class_letter))
        schedule = cursor.fetchall()
        cursor.close()
        return schedule
    finally:
        close_connection(conn)

def get_available_classes(type, class_number=None, class_letter=None):
    conn = get_connection()
    cursor = conn.cursor()

    if type == 'number':
        cursor.execute("SELECT DISTINCT class_number FROM schelude_slots")
    elif type == 'letter' and class_number:
        cursor.execute("SELECT DISTINCT class_letter FROM schelude_slots WHERE class_number = %s", (class_number,))
    elif type == 'day' and class_number:
        cursor.execute("SELECT DISTINCT week_day FROM schelude_slots WHERE class_number = %s AND class_letter = %s", (class_number, class_letter))
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    return [item[0] for item in result]