import sqlite3


# =====================================================
# CREATE DATABASE
# =====================================================

def create_database():

    connection = sqlite3.connect("stories.db")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            prompt TEXT NOT NULL,
            genre TEXT NOT NULL,
            length TEXT NOT NULL,
            tone TEXT NOT NULL,
            story TEXT NOT NULL,
            cover_path TEXT
        )
    """)

    # =================================================
    # OLD DATABASE SUPPORT
    # =================================================

    # Purani stories.db mein agar title column nahi hai
    # to automatically add ho jayega.

    cursor.execute("""
        PRAGMA table_info(stories)
    """)

    columns = [
        column[1]
        for column in cursor.fetchall()
    ]

    # -------------------------------------------------
    # TITLE COLUMN
    # -------------------------------------------------

    if "title" not in columns:

        cursor.execute("""
            ALTER TABLE stories
            ADD COLUMN title TEXT
        """)

    # -------------------------------------------------
    # COVER PATH COLUMN
    # -------------------------------------------------

    if "cover_path" not in columns:

        cursor.execute("""
            ALTER TABLE stories
            ADD COLUMN cover_path TEXT
        """)

    connection.commit()

    connection.close()


# =====================================================
# SAVE STORY
# =====================================================

def save_story(
        title,
        prompt,
        genre,
        length,
        tone,
        story,
        cover_path=None
):

    connection = sqlite3.connect("stories.db")

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO stories
        (
            title,
            prompt,
            genre,
            length,
            tone,
            story,
            cover_path
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        title,
        prompt,
        genre,
        length,
        tone,
        story,
        cover_path
    ))

    connection.commit()

    connection.close()


# =====================================================
# GET STORIES
# =====================================================

def get_stories():

    connection = sqlite3.connect("stories.db")

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            title,
            prompt,
            genre,
            length,
            tone,
            story,
            cover_path
        FROM stories
        ORDER BY id DESC
    """)

    stories = cursor.fetchall()

    connection.close()

    return stories


# =====================================================
# GET SINGLE STORY
# =====================================================

def get_story(story_id):

    connection = sqlite3.connect("stories.db")

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            title,
            prompt,
            genre,
            length,
            tone,
            story,
            cover_path
        FROM stories
        WHERE id = ?
    """, (story_id,))

    story = cursor.fetchone()

    connection.close()

    return story


# =====================================================
# UPDATE STORY
# =====================================================

def update_story(
        story_id,
        title,
        story
):

    connection = sqlite3.connect("stories.db")

    cursor = connection.cursor()

    cursor.execute("""
        UPDATE stories
        SET
            title = ?,
            story = ?
        WHERE id = ?
    """, (
        title,
        story,
        story_id
    ))

    connection.commit()

    connection.close()


# =====================================================
# UPDATE COVER
# =====================================================

def update_cover(
        story_id,
        cover_path
):

    connection = sqlite3.connect("stories.db")

    cursor = connection.cursor()

    cursor.execute("""
        UPDATE stories
        SET cover_path = ?
        WHERE id = ?
    """, (
        cover_path,
        story_id
    ))

    connection.commit()

    connection.close()


# =====================================================
# DELETE STORY
# =====================================================

def delete_story(story_id):

    connection = sqlite3.connect("stories.db")

    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM stories
        WHERE id = ?
    """, (story_id,))

    connection.commit()

    connection.close()