from db_connection import connect_db


def add_student():
    try:
        conn = connect_db()

        if conn is not None:
            cursor = conn.cursor()

            name = input("Enter name: ")
            age = input("Enter age: ")
            city = input("Enter city: ")
            email = input("Enter email: ")
            

            sql = "INSERT INTO student(name,age,city,email) VALUES(%s,%s,%s,%s)"
            cursor.execute(sql, (name,  age, city, email))
            conn.commit()
    except Exception as e:
        print("Error: ", e)
    finally:
        cursor.close()
        conn.close()


def view_student():
    try:
        conn = connect_db()

        if conn is not None:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM student")
            records = cursor.fetchall()
            print("\nID\tName\tAge\tCity\t\tEmail")

            for row in records:
                print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}")

    except Exception as e:
        print("Error: ", e)
    finally:
        cursor.close()
        conn.close()


def update_student():
    try:
        conn = connect_db()

        if conn is not None:
            cursor = conn.cursor()
            sid = int(input("Enter id to be updated: "))
            city = input("Enter new city: ")
            sql = "UPDATE student SET city=%s WHERE id=%s"
            cursor.execute(sql, (city, sid))
            conn.commit()

            if cursor.rowcount == 0:
                print("Student not found")
            else:
                print("Student updated...")

    except Exception as e:
        print("Error: ", e)
    finally:
        cursor.close()
        conn.close()


def delete_student():
    try:
        conn = connect_db()

        if conn is not None:
            cursor = conn.cursor()
            sid = int(input("Enter id to be deleted: "))
            sql = "DELETE FROM student WHERE id=%s"
            cursor.execute(sql, (sid,))
            conn.commit()

            if cursor.rowcount == 0:
                print("Student not found")
            else:
                print("Student deleted...")

    except Exception as e:
        print("Error: ", e)
    finally:
        cursor.close()
        conn.close()


while True:
    print("Student CRUD...")
    print("\n1.Add Student")
    print("2.View Student")
    print("3.Update Student")
    print("4.Delete Student")
    print("5.Exit Student\n")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        view_student()
    elif choice == 3:
        update_student()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        print("Exiting....")
        break
    else:
        print("Invalid choice")
