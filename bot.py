import telebot

TOKEN = "7832232386:AAEXrkVNT8RP709tIJyiI9Qu8yUv3mXLlww"
bot = telebot.TeleBot(TOKEN)

# ---------- trimite plan ----------
def send_plan(chat_id):
    # Mesaj inițial
    bot.send_message(chat_id, "Iată un exemplu de plan 2D. Informațiile sunt în română și rusă.")
    
    # Trimite PDF
    with open("planexemplu.pdf", "rb") as file:
        bot.send_document(chat_id, file)
    
    # Mesaj final
    bot.send_message(
        chat_id,
        "Mulțumim pentru interesul tău!\n\n"
        "Prețul este 15 EUR pe metru pătrat.\n"
        "Avem și variante pentru orice buget, începând de la 3 EUR/m².\n\n"
        "Scrie-ne aici, sau la +37379044935, pentru ofertă personalizată."
    )

# ---------- START (link de pe site) ----------
@bot.message_handler(commands=['start'])
def start_message(message):
    text = message.text

    # dacă vine din link ?start=plan
    if text.startswith("/start plan"):
        send_plan(message.chat.id)
    else:
        bot.send_message(
            message.chat.id,
            "Salut! Apasă linkul de pe site pentru a primi automat un exemplu de plan."
        )

print("Bot online...")
bot.infinity_polling()
