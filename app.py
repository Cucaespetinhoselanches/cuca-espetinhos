import urllib.parse
import streamlit as st

st.set_page_config(
    page_title="Cuca Espetinhos e Lanches", page_icon="🍢", layout="centered"
)

st.title("🍢 Cuca Espetinhos e Lanches")

# Cardápio
menu = {
    "X BURGER": {
        "preco": 19.90,
        "imagem": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400",
    },
    "X SALADA": {
        "preco": 29.90,
        "imagem": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400",
    },
    "X BACON": {
        "preco": 35.90,
        "imagem": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400",
    },
    "X-EGG": {
        "preco": 30.90,
        "imagem": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400",
    },
    "X-CATUPIRY EMPANADO": {
        "preco": 32.90,
        "imagem": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400",
    },
    "FRANGÃO": {
        "preco": 32.90,
        "imagem": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400",
    },
    "PORÇÃO BATATA FRITA": {
        "preco": 29.90,
        "imagem": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400",
    },
    "PORÇÃO MANDIOCA FRITA": {
        "preco": 29.90,
        "imagem": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400",
    },
    "PORÇÃO ANÉIS DE CEBOLA": {
        "preco": 28.90,
        "imagem": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400",
    },
    "PORÇÃO COMBO DE PORÇÕES": {
        "preco": 49.90,
        "imagem": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400",
    },
    "ESPETO PÃO DE ALHO": {
        "preco": 9.00,
        "imagem": "https://espeto.jpg",
    },
    "ESPETO QUEIJO COALHO": {
        "preco": 9.00,
        "imagem": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400",
    },
    "ESPETO PANCETA": {
        "preco": 12.00,
        "imagem": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400",
    },
    "ESPETO ALCATRA": {
        "preco": 12.00,
        "imagem": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400",
    },
    "ESPETO PICANHA": {
        "preco": 18.00,
        "imagem": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400",
    },
    "ESPETO FRALDINHA": {
        "preco": 12.00,
        "imagem": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400",
    },
    "ESPETO LINGUIÇA": {
        "preco": 9.00,
        "imagem": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400",
    },
    "ESPETO LINGUIÇA GOURMET": {
        "preco": 9.00,
        "imagem": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400",
    },
    "ESPETO KAFTA": {
        "preco": 12.00,
        "imagem": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400",
    },
    "ESPETO KAFTA GOURMET": {
        "preco": 12.00,
        "imagem": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400",
    },
    "ESPETO CORAÇÃO": {
        "preco": 18.00,
        "imagem": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400",
    },
    "ESPETO FRANGO": {
        "preco": 12.00,
        "imagem": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400",
    },
    "Refrigerante Lata": {
        "preco": 6.00,
        "imagem": "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=400",
    },
}

carrinho = []
subtotal_produtos = 0.0
taxa_entrega = 5.00  # Valor da taxa de entrega

st.subheader("Faça seu Pedido")

for item, info in menu.items():
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(info["imagem"], width=100)
    with col2:
        qtd = st.number_input(
            f"**{item}** - R$ {info['preco']:.2f}",
            min_value=0,
            step=1,
            key=item,
        )
        if qtd > 0:
            subtotal_item = info["preco"] * qtd
            carrinho.append(
                {"item": item, "qtd": qtd, "subtotal": subtotal_item}
            )
            subtotal_produtos += subtotal_item

if carrinho:
    st.divider()
    st.write(f"### Subtotal dos itens: R$ {subtotal_produtos:.2f}")

    nome = st.text_input("Seu Nome:")
    tipo_entrega = st.radio(
        "Opção de Entrega:",
        ["Entrega", "Retirar no Local"],
        horizontal=True,
    )

    endereco = ""
    total_final = subtotal_produtos

    if tipo_entrega == "Entrega":
        endereco = st.text_input("Endereço de Entrega (Rua, Número, Bairro):")
        total_final += taxa_entrega
        st.info(f"🛵 **Taxa de entrega:** R$ {taxa_entrega:.2f}")
    else:
        st.info("🏪 **Retirada no Balcão:** Sem taxa de entrega.")

    st.write(f"### **Total Final: R$ {total_final:.2f}**")

    pagamento = st.selectbox(
        "Forma de Pagamento", ["Pix", "Cartão", "Dinheiro"]
    )

    pronto_para_enviar = False
    if tipo_entrega == "Entrega":
        if nome and endereco:
            pronto_para_enviar = True
    else:
        if nome:
            pronto_para_enviar = True

    if pronto_para_enviar:
        itens_txt = "\n".join(
            [f"{i['qtd']}x {i['item']} (R$ {i['subtotal']:.2f})" for i in carrinho]
        )

        if tipo_entrega == "Entrega":
            detalhes_tipo = f"*Tipo:* Entrega\n*Endereço:* {endereco}\n*Taxa de Entrega:* R$ {taxa_entrega:.2f}"
        else:
            detalhes_tipo = "*Tipo:* Retirada no Local"

        mensagem = (
            f"Olá! Gostaria de fazer um pedido na *Cuca Espetinhos e Lanches*:\n\n"
            f"*Cliente:* {nome}\n"
            f"{detalhes_tipo}\n"
            f"*Pagamento:* {pagamento}\n\n"
            f"*Itens:*\n{itens_txt}\n\n"
            f"*Total a Pagar:* R$ {total_final:.2f}"
        )

        numero_whatsapp = "5512992093751"
        link = f"https://wa.me/{numero_whatsapp}?text={urllib.parse.quote(mensagem)}"

        st.success("✅ Pedido gerado com sucesso!")
        st.markdown(
            f"[👉 **Clique aqui para abrir o WhatsApp e enviar seu pedido**]({link})",
            unsafe_allow_html=True,
        )
    elif tipo_entrega == "Entrega" and not endereco:
        st.warning("Por favor, preencha o seu nome e o endereço de entrega para prosseguir.")
    elif not nome:
        st.warning("Por favor, preencha o seu nome para prosseguir.")
