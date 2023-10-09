"""Query the database"""

import sqlite3

LOG_FILE = "query_log.md"


def log_query(query):
    with open(LOG_FILE, "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")


def general_query(query):
    conn = sqlite3.connect("Goose.db")
    cursor = conn.cursor()
    cursor.execute(query)
    if (
        query.strip().lower().startswith("insert")
        or query.strip().lower().startswith("update")
        or query.strip().lower().startswith("delete")
    ):
        conn.commit()

    cursor.close()
    conn.close()

    log_query(f"{query}")


def create_record(
    rank,
    username,
    categories,
    subscribers,
    country,
    visits,
    likes,
    comments,
    links,
):
    """create example query"""
    conn = sqlite3.connect("youtubers.db")
    c = conn.cursor()
    c.execute(
        """
        INSERT INTO youtubers
        (rank,username,categories,subscribers,country,visits,likes,comments,links) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            rank,
            username,
            categories,
            subscribers,
            country,
            visits,
            likes,
            comments,
            links,
        ),
    )
    conn.commit()
    conn.close()

    # Log the query
    log_query(
        f"""INSERT INTO youtubers VALUES (
            {rank},
            {username},
            {categories},
            {subscribers},
            {country},
            {visits},
            {likes},
            {comments},
            {links});"""
    )


def update_record(
    rank,
    username,
    categories,
    subscribers,
    country,
    visits,
    likes,
    comments,
    links,
):
    """update example query"""
    conn = sqlite3.connect("youtubers.db")
    c = conn.cursor()
    c.execute(
        """
        UPDATE youtubers 
        rank=?,
        username=?,
        categories=?,
        subscribers=?,
        country=?,
        visits=?,
        likes=?,
        comments=?,
        links=?,
        """,
        (
            rank,
            username,
            categories,
            subscribers,
            country,
            visits,
            likes,
            comments,
            links
        ),
    )
    conn.commit()
    conn.close()

    # Log the query
    log_query(
        f"""UPDATE Goose SET
        rank={rank},
        username={username},
        categories={categories},
        subscribers={subscribers},
        country={country},
        visits={visits},
        likes={likes},
        comments={comments},
        links={links},
        WHERE id={record_id};"""
    )


def delete_record(record_id):
    """delete example query"""
    conn = sqlite3.connect("youtubers.db")
    c = conn.cursor()
    c.execute("DELETE FROM youtubers WHERE id=?", (record_id,))
    conn.commit()
    conn.close()

    # Log the query
    log_query(f"DELETE FROM youtubers WHERE id={record_id};")


def read_data():
    """read data"""
    conn = sqlite3.connect("youtubers.db")
    c = conn.cursor()
    c.execute("SELECT * FROM youtubers")
    data = c.fetchall()
    log_query("SELECT * FROM youtubers;")
    return data
