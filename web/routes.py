from flask import render_template, request, redirect, session
from web import web
from web.auth import login_required

from database.users import count_users, get_all_users
from database.admins import add_admin, remove_admin, get_all_admins
from database.files import count_files, get_file, increment_download
from database.premium import get_all_premium
from database.settings import get_settings, update_settings
from database.logs import get_logs


# 🔐 LOGIN
@web.route("/login", methods=["GET", "POST"])
async def login():
    if request.method == "POST":
        password = request.form.get("password")

        if password == "admin123":  # change in production
            session["admin"] = True
            return redirect("/")

    return render_template("login.html")


# 🔓 LOGOUT
@web.route("/logout")
async def logout():
    session.clear()
    return redirect("/login")


# 📊 DASHBOARD
@web.route("/")
@login_required
async def dashboard():
    users = await count_users()
    files = await count_files()
    settings = await get_settings()

    return render_template(
        "dashboard.html",
        users=users,
        files=files,
        settings=settings
    )


# 👮 ADMIN PANEL
@web.route("/admins", methods=["GET", "POST"])
@login_required
async def admins():

    if request.method == "POST":
        user_id = int(request.form.get("user_id"))
        action = request.form.get("action")

        if action == "add":
            await add_admin(user_id)
        elif action == "remove":
            await remove_admin(user_id)

        return redirect("/admins")

    admins = await get_all_admins().to_list(length=100)
    return render_template("admins.html", admins=admins)


# 👥 USERS PAGE
@web.route("/users")
@login_required
async def users_page():
    users = await get_all_users().to_list(length=200)
    return render_template("users.html", users=users)


# 💎 PREMIUM PAGE
@web.route("/premium")
@login_required
async def premium_page():
    premium = await get_all_premium().to_list(length=100)
    return render_template("premium.html", premium=premium)


# ⚙ SETTINGS PAGE
@web.route("/settings", methods=["GET", "POST"])
@login_required
async def settings_page():

    if request.method == "POST":
        force_channel = request.form.get("force_channel")
        force_join = True if request.form.get("force_join") else False

        await update_settings({
            "force_channel": force_channel,
            "force_join_request": force_join
        })

        return redirect("/settings")

    settings = await get_settings()
    return render_template("settings.html", settings=settings)


# 📢 BROADCAST PAGE
@web.route("/broadcast", methods=["GET", "POST"])
@login_required
async def broadcast_page():

    if request.method == "POST":
        from plugins.broadcast import broadcast_handler
        message = request.form.get("message")
        # You can implement proper web broadcast logic
        return redirect("/broadcast")

    return render_template("broadcast.html")


# 📝 LOGS PAGE
@web.route("/logs")
@login_required
async def logs_page():
    logs = await get_logs(100)
    logs = await logs.to_list(length=100)
    return render_template("logs.html", logs=logs)


# 📂 FILE STREAM
@web.route("/file/<file_id>")
async def stream_file(file_id):

    file = await get_file(file_id)

    if not file:
        return "File Not Found"

    await increment_download(file_id)

    return f"Streaming file: {file['file_name']}"
