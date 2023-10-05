from database import get_db_connection

db_connection = get_db_connection
cursor = db_connection.cursor(dictionary=True)

class Wordpress_profile:
    def __init__(self):
        return
    
    def get_all_profiles(self):
        """
        Get a Wordpress profiles
        """
        query = "SELECT * FROM Wordpress_profile"
        cursor.execute(query)
        profiles = cursor.fetchall()
        if not profiles:
            return
        return profiles

    def get_by_id(self, uniqueId):
        """
        Get a Wordpress profile by unique id
        """
        query = "SELECT * FROM Wordpress_profile WHERE uniqueId = %s"
        cursor.execute(query, (uniqueId,))
        profile = cursor.fetchone()
        if not profile:
            return
        return profile