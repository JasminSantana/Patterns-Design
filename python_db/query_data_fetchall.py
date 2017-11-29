from config import config
import psycopg2

""""Author: Santana Mares Jasmin
    gmail: sant.mar.1997@gmail.com
    """


def get_parts():
    """ Query parts from the parts table """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT part_id, part_name FROM parts ORDER BY part_name")
        rows = cur.fetchall()
        print("The number of parts: ", cur.rowcount)
        for row in rows:
            print(row)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    get_parts()
