from app.core.language_manager import language_manager


TRANSLATIONS = {

    "en": {

        "login": "Login",
        "create_account": "Create Account",
        "full_name": "Full Name",
        "email": "Email",
        "password": "Password",
        "confirm_password": "Confirm Password",
        "back": "Back",
        "change_language": "Change Language",
        "chat": "Chat",
        "legal_documents": "Legal Documents",
        "settings": "Settings",
        "import_document": "Import Document",
        "about": "About",
        "chat_with_raphael": "Chat with Raphael",
        "ask": "Ask",
        "interface_language": "Interface Language",
        "status_ready": "Status: Ready",

    },

    "fr": {

        "login": "Connexion",
        "create_account": "Créer un compte",
        "full_name": "Nom complet",
        "email": "E-mail",
        "password": "Mot de passe",
        "confirm_password": "Confirmer le mot de passe",
        "back": "Retour",
        "change_language": "Changer la langue",
        "chat": "Discussion",
        "legal_documents": "Documents juridiques",
        "settings": "Paramètres",
        "import_document": "Importer un document",
        "about": "À propos",
        "chat_with_raphael": "Discuter avec Raphael",
        "ask": "Envoyer",
        "interface_language": "Langue de l'interface",
        "status_ready": "Statut : Prêt",

    },

    "ar": {

        "login": "تسجيل الدخول",
        "create_account": "إنشاء حساب",
        "full_name": "الاسم الكامل",
        "email": "البريد الإلكتروني",
        "password": "كلمة المرور",
        "confirm_password": "تأكيد كلمة المرور",
        "back": "رجوع",
        "change_language": "تغيير اللغة",
        "chat": "المحادثة",
        "legal_documents": "الوثائق القانونية",
        "settings": "الإعدادات",
        "import_document": "استيراد وثيقة",
        "about": "حول",
        "chat_with_raphael": "المحادثة مع رافاييل",
        "ask": "إرسال",
        "interface_language": "لغة الواجهة",
        "status_ready": "الحالة: جاهز",

    }

}

def t(key):

    language = language_manager.get_interface_language()

    language_pack = TRANSLATIONS.get(
        language,
        TRANSLATIONS["en"]
    )

    return language_pack.get(
        key,
        TRANSLATIONS["en"].get(key, key)
    )

    

