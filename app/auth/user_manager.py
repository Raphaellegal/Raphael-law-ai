from app.database.database import get_connection
from app.auth.password import hash_password, verify_password
from app.database.models import User


class UserManager:


    def create_user(self, user):

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(

            """
            INSERT INTO users(

                full_name,
                email,
                password_hash,
                category,
                role,
                verified,
                verification_status,
                subscription

            )

            VALUES (?, ?, ?, ?, ?, ?, ?, ?)

            """,

            (

                user.full_name,
                user.email,
                user.password_hash,
                user.category,
                user.role,
                int(user.verified),
                user.verification_status,
                user.subscription

            )

        )

        connection.commit()

        connection.close()


    def authenticate(self, email, password):

        user = self.get_user_by_email(email)


        if not user:

            return None


        if verify_password(
            password,
            user.password_hash
        ):

            return user


        return None


    def get_user_by_email(self, email):

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                id,
                full_name,
                email,
                password_hash,
                category,
                role,
                verified,
                verification_status,
                subscription

            FROM users

            WHERE email = ?
            """,
            (email,)
        )

        row = cursor.fetchone()

        connection.close()


        if row:

            return User(

                id=row[0],

                full_name=row[1],

                email=row[2],

                password_hash=row[3],

                category=row[4],

                role=row[5],

                verified=bool(row[6]),

                verification_status=row[7],

                subscription=row[8]

            )


        return None


user_manager = UserManager()