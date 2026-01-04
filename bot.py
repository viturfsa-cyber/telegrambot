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

TOKEN = "8531539087:AAEMqvqtXZS82RmazqdWe9AO2XC9hxDP_hE"

LINK_SEMANAL = "https://mpago.la/1LEY4CP"
LINK_MENSAL = "https://mpago.la/2oL26cr"

# ======================
# /start
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
        parse_mode="Markdown"
    )

# ======================
# PRÉVIAS (SÓ TEXTO)
# ======================

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
        parse_mode="Markdown"
    )

# ======================
# JÁ PAGUEI
# ======================

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
        parse_mode="Markdown"
    )

# ======================
# MAIN
# ======================

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(previas, pattern="previas"))
    app.add_handler(CallbackQueryHandler(ja_paguei, pattern="ja_paguei"))

    print("🤖 Bot rodando...")
    app.run_polling()

if __name__ == "__main__":
    main()
    


