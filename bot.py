import asyncio
from flask import Flask
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

# ======================
# CONFIGURAÇÕES
# ======================

TOKEN = "AAEMqvqtXZS82RmazqdWe9AO2XC9hxDP_hE"

LINK_SEMANAL = "https://mpago.la/1LEY4CP"
LINK_MENSAL = "https://mpago.la/2oL26cr"

# ======================
# FLASK APP
# ======================

app = Flask(__name__)

@app.route("/")
def home():
    return "🤖 Bot está rodando no Render!"

# ======================
# HANDLERS TELEGRAM
# ======================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🔞 *ENTRE PARA O GRUPO VIP* 🔞\n\n"
        "🔥 *O QUE VOCÊ VAI RECEBER* 🔥\n"
        "✅ Acesso imediato ao grupo fechado\n"
        "✅ Conteúdos exclusivos\n"
        "✅ Material que não fica público\n"
        "✅ Comunidade restrita\n\n"
        "⚡ A liberação ocorre automaticamente após a confirmação do pagamento.\n\n"
        "🔒 Pagamento 100% seguro via Mercado Pago\n\n"
        "👇 Escolha uma opção abaixo"
    )

    keyboard = [
        [InlineKeyboardButton("👀 Ver Prévias", callback_data="previas")],
        [InlineKeyboardButton("Plano Semanal – R$19", url=LINK_SEMANAL)],
        [InlineKeyboardButton("Plano Mensal – R$39 🔥", url=LINK_MENSAL)],
        [InlineKeyboardButton("✅ Já paguei", callback_data="ja_paguei")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        text=text,
        reply_markup=reply_markup,
        parse_mode="MarkdownV2"
    )

async def previas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    text = (
        "🚫 *Este conteúdo não pode ser exibido fora do ambiente VIP.*\n\n"
        "⚠️ *Prévia bloqueada por conter material sensível.*\n\n"
        "O conteúdo completo:\n"
        "• É restrito\n"
        "• Não fica público\n"
        "• Foi removido de várias plataformas\n\n"
        "👇 Escolha um plano abaixo para liberar o acesso"
    )

    keyboard = [
        [InlineKeyboardButton("Plano Semanal – R$19", url=LINK_SEMANAL)],
        [InlineKeyboardButton("Plano Mensal – R$39 🔥", url=LINK_MENSAL)],
        [InlineKeyboardButton("✅ Já paguei", callback_data="ja_paguei")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.message.reply_text(
        text=text,
        reply_markup=reply_markup,
        parse_mode="MarkdownV2"
    )

async def ja_paguei(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    text = (
        "⏳ *Pagamento identificado em processamento.*\n\n"
        "⚡ A confirmação ocorre automaticamente.\n"
        "🔓 A liberação do acesso acontece em até *10 minutos*.\n\n"
        "Se o acesso não for liberado nesse prazo, aguarde — "
        "pagamentos via PIX ou cartão podem levar alguns minutos.\n\n"
        "Obrigado pela confiança."
    )

    await query.message.reply_text(
        text=text,
        parse_mode="MarkdownV2"
    )

# ======================
# MAIN
# ======================

async def run_bot():
    app_tg = ApplicationBuilder().token(TOKEN).build()

    app_tg.add_handler(CommandHandler("start", start))
    app_tg.add_handler(CallbackQueryHandler(previas, pattern="previas"))
    app_tg.add_handler(CallbackQueryHandler(ja_paguei, pattern="ja_paguei"))

    print("🤖 Bot rodando...")
    await app_tg.run_polling()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(run_bot())
    # Flask abre a porta para Render detectar
    app.run(host="0.0.0.0", port=10000)
