import urllib.parse
import streamlit as st

# ==================== FUNÇÃO DO MODAL DE CONFIRMAÇÃO ====================
@st.dialog("📋 Confirmar e Enviar Pedido")
def modal_confirmacao(numero_wa, mensagem_texto):
    st.write("### Revise os detalhes do seu pedido:")
    st.info(mensagem_texto)

    link_whatsapp = f"https://wa.me/{numero_wa}?text={urllib.parse.quote(mensagem_texto)}"

    st.write("---")
    col_voltar, col_enviar = st.columns([1, 2])

    with col_voltar:
        if st.button("❌ Alterar Pedido", use_container_width=True):
            st.session_state["mostrar_modal"] = False
            st.rerun()

    with col_enviar:
        st.link_button(
            "📲 CONFIRMAR E ENVIAR",
            link_whatsapp,
            type="primary",
            use_container_width=True,
        )
# =======================================================================

st.set_page_config(
    page_title="Cuca Espetinhos e Lanches", page_icon="🍢", layout="centered"
)

# --- ESTILIZAÇÃO DO BOTÃO WHATSAPP (VERDE E GRANDE) ---
st.markdown("""
    <style>
    div.stLinkButton > a[kind="primary"], div.stButton > button[kind="primary"] {
        width: 100% !important;
        height: 3.5em !important;
        font-size: 20px !important;
        font-weight: bold !important;
        background-color: #25D366 !important; /* Verde oficial WhatsApp */
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
    }
    div.stLinkButton > a[kind="primary"]:hover, div.stButton > button[kind="primary"]:hover {
        background-color: #1EBE5D !important;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# Exibe o logo local salvo na pasta do projeto
st.image("logo.png", width=200)

st.title("🍢 Cuca Espetinhos e Lanches")

# Cardápio
menu = {
    "X BURGER": {
        "preco": 19.90,
        "imagem": "https://plus.unsplash.com/premium_photo-1675252369719-dd52bc69c3df?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8ZXNwZXRvJTIwZGUlMjBjYXJuZXxlbnwwfHwwfHx8MA%3D%3D",
    },
    "X SALADA": {
        "preco": 29.90,
        "imagem": "https://plus.unsplash.com/premium_photo-1675252369719-dd52bc69c3df?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8ZXNwZXRvJTIwZGUlMjBjYXJuZXxlbnwwfHwwfHx8MA%3D%3D",
    },
    "X BACON": {
        "preco": 35.90,
        "imagem": "https://plus.unsplash.com/premium_photo-1675252369719-dd52bc69c3df?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8ZXNwZXRvJTIwZGUlMjBjYXJuZXxlbnwwfHwwfHx8MA%3D%3D",
    },
    "X-EGG": {
        "preco": 30.90,
        "imagem": "https://plus.unsplash.com/premium_photo-1675252369719-dd52bc69c3df?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8ZXNwZXRvJTIwZGUlMjBjYXJuZXxlbnwwfHwwfHx8MA%3D%3D",
    },
    "X-CATUPIRY EMPANADO": {
        "preco": 32.90,
        "imagem": "https://plus.unsplash.com/premium_photo-1675252369719-dd52bc69c3df?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8ZXNwZXRvJTIwZGUlMjBjYXJuZXxlbnwwfHwwfHx8MA%3D%3D",
    },
    "FRANGÃO": {
        "preco": 32.90,
        "imagem": "https://plus.unsplash.com/premium_photo-1675252369719-dd52bc69c3df?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8ZXNwZXRvJTIwZGUlMjBjYXJuZXxlbnwwfHwwfHx8MA%3D%3D",
    },
    "HOT CALABRESA": {
        "preco": 16.50,
        "imagem": "https://images.unsplash.com/photo-1613482084286-41f25b486fa2?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8SE9UJTIwRE9HfGVufDB8fDB8fHww",
    },
    "HOT BACON": {
        "preco": 16.50,
        "imagem": "https://images.unsplash.com/photo-1613482084286-41f25b486fa2?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8SE9UJTIwRE9HfGVufDB8fDB8fHww",
    },
    "HOT SALADA": {
        "preco": 12.50,
        "imagem": "https://images.unsplash.com/photo-1613482084286-41f25b486fa2?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8SE9UJTIwRE9HfGVufDB8fDB8fHww",
    },
    "HOT PURE": {
        "preco": 14.50,
        "imagem": "https://images.unsplash.com/photo-1613482084286-41f25b486fa2?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8SE9UJTIwRE9HfGVufDB8fDB8fHww",
    },
    "PORÇÃO BATATA FRITA": {
        "preco": 29.90,
        "imagem": "https://plus.unsplash.com/premium_photo-1672774750509-bc9ff226f3e8?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8cG9yJUMzJUE3JUMzJUE3byUyMGJhdGF0YSUyMGZyaXRhfGVufDB8fDB8fHww",
    },
    "PORÇÃO MANDIOCA FRITA": {
        "preco": 29.90,
        "imagem": "https://media.istockphoto.com/id/903103922/pt/foto/brazilian-food-mandioca-frita-deep-fried-cassava-root.webp?a=1&b=1&s=612x612&w=0&k=20&c=KwVZFUrGJlRkXM6_nyBNPt_6sbpHJ1x0pR49fA2wIgY=",
    },
    "PORÇÃO ANÉIS DE CEBOLA": {
        "preco": 28.90,
        "imagem": "https://images.unsplash.com/photo-1766589152292-3c052f0d87aa?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fHBvciVDMyVBNyVDMyVBM28lMjBhbmVpcyUyMGRlJTIwY2Vib2xhfGVufDB8fDB8fHww",
    },
    "PORÇÃO COMBO DE PORÇÕES": {
        "preco": 49.90,
        "imagem": "https://images.unsplash.com/photo-1702827495434-629df15aa136?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDB8fHBvciVDMyVBNyVDMyVBM28lMjBjb21ib3xlbnwwfHwwfHx8MA%3D%3D",
    },
    "ESPETO PÃO DE ALHO": {
        "preco": 9.00,
        "imagem": "https://plus.unsplash.com/premium_photo-1661310177352-f586bf23a403?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    },
    "ESPETO ROMEU E JULIETA (Bacon/Goiabada/Queijo)": {
        "preco": 15.00,
        "imagem": "https://plus.unsplash.com/premium_photo-1661310177352-f586bf23a403?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    },
    "ESPETO QUEIJO COALHO": {
        "preco": 9.00,
        "imagem": "https://plus.unsplash.com/premium_photo-1661310177352-f586bf23a403?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    },
    "ESPETO PANCETA": {
        "preco": 12.00,
        "imagem": "https://plus.unsplash.com/premium_photo-1661310177352-f586bf23a403?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    },
    "ESPETO ALCATRA": {
        "preco": 12.00,
        "imagem": "https://plus.unsplash.com/premium_photo-1661310177352-f586bf23a403?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    },
    "ESPETO PICANHA": {
        "preco": 18.00,
        "imagem": "https://plus.unsplash.com/premium_photo-1661310177352-f586bf23a403?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    },
    "ESPETO FRALDINHA": {
        "preco": 12.00,
        "imagem": "https://plus.unsplash.com/premium_photo-1661310177352-f586bf23a403?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    },
    "ESPETO LINGUIÇA": {
        "preco": 9.00,
        "imagem": "https://plus.unsplash.com/premium_photo-1661310177352-f586bf23a403?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    },
    "ESPETO LINGUIÇA GOURMET": {
        "preco": 9.00,
        "imagem": "https://plus.unsplash.com/premium_photo-1661310177352-f586bf23a403?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    },
    "ESPETO KAFTA": {
        "preco": 12.00,
        "imagem": "https://plus.unsplash.com/premium_photo-1661310177352-f586bf23a403?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    },
    "ESPETO KAFTA GOURMET": {
        "preco": 12.00,
        "imagem": "https://plus.unsplash.com/premium_photo-1661310177352-f586bf23a403?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    },
    "ESPETO CORAÇÃO": {
        "preco": 18.00,
        "imagem": "https://plus.unsplash.com/premium_photo-1661310177352-f586bf23a403?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    },
    "ESPETO FRANGO": {
        "preco": 12.00,
        "imagem": "https://plus.unsplash.com/premium_photo-1661310177352-f586bf23a403?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    },
    "Refrigerante Lata": {
        "preco": 6.00,
        "imagem": "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=400",
    },
    "Suco Del Valle 200ml": {
        "preco": 8.00,
        "imagem": "https://images.unsplash.com/photo-1613478223719-2ab802602423?w=400",
    },
    "Suco 1L": {
        "preco": 10.00,
        "imagem": "https://images.unsplash.com/photo-1613478223719-2ab802602423?w=400",
    },
    "Cerveja Original 300ml Garrafinha": {
        "preco": 6.00,
        "imagem": "https://th.bing.com/th/id/OIP.yv46CREzjTxIfnQpp9lU5wHaHa?w=184&h=187&c=7&r=0&o=7&pid=1.7&rm=3",
    },
    "Cerveja Budweiser 300ml Garrafinha": {
        "preco": 6.00,
        "imagem": "https://th.bing.com/th/id/OIP.yv46CREzjTxIfnQpp9lU5wHaHa?w=184&h=187&c=7&r=0&o=7&pid=1.7&rm=3",
    },
    "Cerveja Antarctica 300ml Garrafinha": {
        "preco": 5.00,
        "imagem": "https://th.bing.com/th/id/OIP.yv46CREzjTxIfnQpp9lU5wHaHa?w=184&h=187&c=7&r=0&o=7&pid=1.7&rm=3",
    },
    "Cerveja Brahma 300ml Garrafinha": {
        "preco": 5.00,
        "imagem": "https://th.bing.com/th/id/OIP.yv46CREzjTxIfnQpp9lU5wHaHa?w=184&h=187&c=7&r=0&o=7&pid=1.7&rm=3",
    },
    "Cerveja Império 300ml Garrafinha": {
        "preco": 5.00,
        "imagem": "https://th.bing.com/th/id/OIP.yv46CREzjTxIfnQpp9lU5wHaHa?w=184&h=187&c=7&r=0&o=7&pid=1.7&rm=3",
    },
    "Cerveja Skol 269ml Lata": {
        "preco": 5.00,
        "imagem": "https://tse4.mm.bing.net/th/id/OIP.Cqa-Rx_ea-YoraLE7dVVpQHaFj?r=0&pid=ImgDet&w=204&h=153&c=7&o=7&rm=3",
    },
    "Cerveja Budweiser 269ml Lata": {
        "preco": 6.00,
        "imagem": "https://tse4.mm.bing.net/th/id/OIP.Cqa-Rx_ea-YoraLE7dVVpQHaFj?r=0&pid=ImgDet&w=204&h=153&c=7&o=7&rm=3",
    },
    "Cerveja Original 269ml Lata": {
        "preco": 6.00,
        "imagem": "https://tse4.mm.bing.net/th/id/OIP.Cqa-Rx_ea-YoraLE7dVVpQHaFj?r=0&pid=ImgDet&w=204&h=153&c=7&o=7&rm=3",
    },
    "Cerveja Amstel 269ml Lata": {
        "preco": 5.00,
        "imagem": "https://tse4.mm.bing.net/th/id/OIP.Cqa-Rx_ea-YoraLE7dVVpQHaFj?r=0&pid=ImgDet&w=204&h=153&c=7&o=7&rm=3",
    },
    "Cerveja Império 269ml Lata": {
        "preco": 5.00,
        "imagem": "https://tse4.mm.bing.net/th/id/OIP.Cqa-Rx_ea-YoraLE7dVVpQHaFj?r=0&pid=ImgDet&w=204&h=153&c=7&o=7&rm=3",
    },
    "Cerveja Brahma Duplo Malte 269ml Lata": {
        "preco": 6.00,
        "imagem": "https://tse4.mm.bing.net/th/id/OIP.Cqa-Rx_ea-YoraLE7dVVpQHaFj?r=0&pid=ImgDet&w=204&h=153&c=7&o=7&rm=3",
    },
    "Cerveja Long Neck Heineken": {
        "preco": 10.00,
        "imagem": "https://images.unsplash.com/photo-1618885472179-5e474019f2a9?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8Z2FycmFmYSUyMGRlJTIwY2VydmVqYXxlbnwwfHwwfHx8MA%3D%3D",
    },
    "Cerveja Long Neck Budweiser": {
        "preco": 10.00,
        "imagem": "https://images.unsplash.com/photo-1587669284207-e8ee0fc74144?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8Z2FycmFmYSUyMGRlJTIwY2VydmVqYXxlbnwwfHwwfHx8MA%3D%3D",
    },
    "Cerveja Long Neck Corona": {
        "preco": 10.00,
        "imagem": "https://images.unsplash.com/photo-1600213903598-25be92abde40?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8Z2FycmFmYSUyMGRlJTIwY2VydmVqYXxlbnwwfHwwfHx8MA%3D%3D",
    },
    "Energético Monster 473ml": {
        "preco": 14.00,
        "imagem": "https://images.unsplash.com/photo-1622543925917-763c34d1a86e?w=400",
    },
    "Cerveja Amstel 350ml Lata": {
        "preco": 6.00,
        "imagem": "https://tse4.mm.bing.net/th/id/OIP.Cqa-Rx_ea-YoraLE7dVVpQHaFj?r=0&pid=ImgDet&w=204&h=153&c=7&o=7&rm=3",
    },
    "Cerveja Império 350ml Lata": {
        "preco": 6.00,
        "imagem": "https://tse4.mm.bing.net/th/id/OIP.Cqa-Rx_ea-YoraLE7dVVpQHaFj?r=0&pid=ImgDet&w=204&h=153&c=7&o=7&rm=3",
    },
    "Cerveja Brahma Duplo Malte 350ml Lata": {
        "preco": 7.00,
        "imagem": "https://tse4.mm.bing.net/th/id/OIP.Cqa-Rx_ea-YoraLE7dVVpQHaFj?r=0&pid=ImgDet&w=204&h=153&c=7&o=7&rm=3",
    },
}

# Tabela de Bairros e Taxas de Entrega
taxas_bairros = {
    "Nova Jacareí": 3.00,
    "Igarapés": 5.00,
    "Esperança": 4.00,
    "São Luiz": 5.00,
    "Portal": 5.00,
    "Jardim São Paulo": 5.00,
    "Terras de São João": 5.00,
    "1º de Maio": 5.00,
    "Jardim Alvorada": 5.00,
    "Imperial": 5.00,
    "Pedramar": 7.00,
    "Ijal": 5.00,
    "São João": 6.00,
    "Centro": 8.00,
    "Panorama": 7.00,
    "Jardim Dindinha": 7.00,
    "Jardim Emília": 7.00,
    "Outro Bairro (A combinar)": 0.00,
}

carrinho = []
subtotal_produtos = 0.0

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
    taxa_entrega = 0.00
    total_final = subtotal_produtos

    if tipo_entrega == "Entrega":
        bairro = st.selectbox("Selecione o seu Bairro:", list(taxas_bairros.keys()))
        taxa_entrega = taxas_bairros[bairro]
        rua_numero = st.text_input("Rua e Número:")

        if rua_numero:
            endereco = f"{rua_numero} - {bairro}"

        total_final += taxa_entrega
        if taxa_entrega > 0:
            st.info(f"🛵 **Taxa de entrega para {bairro}:** R$ {taxa_entrega:.2f}")
        else:
            st.warning("⚠️ Taxa de entrega para este bairro será confirmada pelo WhatsApp.")
    else:
        st.info("🏪 **Retirada no Balcão:** Sem taxa de entrega.")

    st.write(f"### **Total Final: R$ {total_final:.2f}**")

    pagamento = st.selectbox(
        "Forma de Pagamento", ["Pix", "Cartão", "Dinheiro"]
    )

    pronto_para_enviar = False
    if tipo_entrega == "Entrega":
        if nome and rua_numero:
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

        # Botão para o usuário acionar o modal
        if st.button("🚀 AVANÇAR PARA CONFIRMAÇÃO", type="primary", use_container_width=True):
            st.session_state["mostrar_modal"] = True

        # Exibe o modal apenas quando ativado pelo session_state
        if st.session_state.get("mostrar_modal", False):
            modal_confirmacao(numero_whatsapp, mensagem)

    elif tipo_entrega == "Entrega" and not rua_numero:
        st.warning("Por favor, preencha o seu nome, selecione o bairro e informe a rua e número.")
    elif not nome:
        st.warning("Por favor, preencha o seu nome para prosseguir.")
