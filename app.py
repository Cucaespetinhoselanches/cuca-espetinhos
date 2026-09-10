import urllib.parse
import streamlit as st

# ==================== ESTADOS DA SESSÃO ====================
if "mostrar_modal" not in st.session_state:
    st.session_state["mostrar_modal"] = False

# Controla a exibição das etapas do formulário
if "etapa_pedido" not in st.session_state:
    st.session_state["etapa_pedido"] = "cardapio"  # 'cardapio' ou 'dados_entrega'

# ==================== FUNÇÃO DO MODAL DE CONFIRMAÇÃO ====================
@st.dialog("📋 Confirmar e Enviar Pedido")
def modal_confirmacao(numero_wa, mensagem_texto):
    st.markdown(
        "<h3 style='color: #000000; font-weight: 800; margin-bottom: 15px;'>"
        "📋 Revise os detalhes do seu pedido:"
        "</h3>",
        unsafe_allow_html=True,
    )
    st.info(mensagem_texto)

    link_whatsapp = (
        f"https://wa.me/{numero_wa}?text={urllib.parse.quote(mensagem_texto)}"
    )

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

# --- ESTILIZAÇÃO CUSTOMIZADA DE FONTES E BOTÕES ---
st.markdown(
    """
    <style>
    /* Aumenta a fonte geral dos rótulos de campos e entradas */
    label, div[data-testid="stMarkdownContainer"] p {
        font-size: 18px !important;
    }

    /* Aumenta os títulos das seções */
    h1 { font-size: 32px !important; }
    h2 { font-size: 26px !important; }
    h3 { font-size: 22px !important; }

    /* Destaque para os preços nos itens */
    .preco-destaque {
        font-size: 20px !important;
        font-weight: bold !important;
        color: #2e7d32 !important;
    }

    /* Estilização padrão de botões */
    div.stButton > button {
        font-size: 18px !important;
        font-weight: bold !important;
        min-height: 3em !important;
        border-radius: 10px !important;
    }

    /* Estilização dos botões principais */
    div.stLinkButton > a[kind="primary"], div.stButton > button[kind="primary"] {
        width: 100% !important;
        height: 3.5em !important;
        background-color: #25D366 !important;
        border: none !important;
        border-radius: 12px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }

    div.stLinkButton > a[kind="primary"] p, div.stButton > button[kind="primary"] p {
        font-size: 22px !important;
        font-weight: 900 !important;
        color: #0b3d18 !important;
    }
    
    /* Aumenta a fonte e o contraste do texto exibido no resumo do pedido (st.info) */
    div[data-testid="stNotification"] {
        background-color: #e3f2fd !important;
        border-left-color: #0d47a1 !important;
    }

    div[data-testid="stNotification"] p {
        font-size: 20px !important;
        font-weight: 600 !important;
        color: #000000 !important;
        line-height: 1.6 !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

st.image("logo.png", width=200)
st.title("🍢 Cuca Espetinhos e Lanches")

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
    "HOT CALABRESA": {
        "preco": 16.50,
        "imagem": "https://images.unsplash.com/photo-1613482084286-41f25b486fa2?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8SE9UJTIwRE9HfGVufDB8fDB8fHww",
    },
    "Refrigerante Lata": {
        "preco": 6.00,
        "imagem": "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=400",
    },
}

taxas_bairros = {
    "Nova Jacareí": 3.00,
    "Igarapés": 5.00,
    "Esperança": 4.00,
    "Centro": 8.00,
    "Outro Bairro (A combinar)": 0.00,
}

carrinho = []
subtotal_produtos = 0.0

st.subheader("Faça seu Pedido")

# Exibe o cardápio
for item, info in menu.items():
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(info["imagem"], width=100)
    with col2:
        label_item = f"**{item}** — <span class='preco-destaque'>R$ {info['preco']:.2f}</span>"
        st.markdown(label_item, unsafe_allow_html=True)
        qtd = st.number_input(
            "Quantidade:",
            min_value=0,
            step=1,
            key=item,
            label_visibility="collapsed",
        )
        if qtd > 0:
            subtotal_item = info["preco"] * qtd
            carrinho.append(
                {"item": item, "qtd": qtd, "subtotal": subtotal_item}
            )
            subtotal_produtos += subtotal_item

# Caso o usuário tenha selecionado ao menos 1 item
if carrinho:
    st.divider()
    st.write(f"## **Subtotal dos itens: R$ {subtotal_produtos:.2f}**")

    # PERGUNTA E BOTÕES DE AÇÃO INTERATIVOS
    st.markdown("### **Deseja incluir mais itens ao seu pedido?**")
    col_btn_mais, col_btn_encerrar = st.columns(2)

    with col_btn_mais:
        if st.button("➕ Inserir Mais Produtos", use_container_width=True):
            st.session_state["etapa_pedido"] = "cardapio"
            st.toast(
                "Continue escolhendo seus itens no cardápio acima!", icon="🛒"
            )

    with col_btn_encerrar:
        if st.button(
            "✅ Encerrar Pedido", type="primary", use_container_width=True
        ):
            st.session_state["etapa_pedido"] = "dados_entrega"

    # Exibe a etapa de endereço/pagamento quando o usuário clica em Encerrar
    if st.session_state["etapa_pedido"] == "dados_entrega":
        st.write("---")
        st.subheader("📦 Dados de Entrega e Pagamento")

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
            bairro = st.selectbox(
                "Selecione o seu Bairro:", list(taxas_bairros.keys())
            )
            taxa_entrega = taxas_bairros[bairro]
            rua_numero = st.text_input("Rua e Número:")

            if rua_numero:
                endereco = f"{rua_numero} - {bairro}"

            total_final += taxa_entrega
            if taxa_entrega > 0:
                st.info(
                    f"🛵 **Taxa de entrega para {bairro}:** R$ {taxa_entrega:.2f}"
                )
            else:
                st.warning(
                    "⚠️ Taxa de entrega para este bairro será confirmada pelo WhatsApp."
                )
        else:
            st.info("🏪 **Retirada no Balcão:** Sem taxa de entrega.")

        st.write(f"## **Total Final: R$ {total_final:.2f}**")

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
                [
                    f"{i['qtd']}x {i['item']} (R$ {i['subtotal']:.2f})"
                    for i in carrinho
                ]
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

            if st.button(
                "🚀 AVANÇAR PARA CONFIRMAÇÃO",
                type="primary",
                use_container_width=True,
            ):
                st.session_state["mostrar_modal"] = True

            if st.session_state.get("mostrar_modal", False):
                modal_confirmacao(numero_whatsapp, mensagem)

        elif tipo_entrega == "Entrega" and not rua_numero:
            st.warning("Por favor, informe seu nome, rua e número para enviar.")
        elif not nome:
            st.warning("Por favor, preencha o seu nome para liberar o pedido.")
