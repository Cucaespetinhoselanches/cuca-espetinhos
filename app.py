import urllib.parse
import streamlit as st

st.set_page_config(
    page_title="Cuca Espetinhos e Lanches", page_icon="🍢", layout="centered"
)

# --- ESTILIZAÇÃO CSS (Botão do WhatsApp em Destaque) ---
st.markdown(
    """
    <style>
    /* Estiliza o botão final de envio do WhatsApp para ter destaque total */
    div.stLinkButton > a[kind="primary"], div.stButton > button[kind="primary"] {
        width: 100% !important;
        height: 3.5em !important;
        font-size: 20px !important;
        font-weight: bold !important;
        background-color: #25D366 !important; /* Verde WhatsApp */
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    div.stLinkButton > a[kind="primary"]:hover, div.stButton > button[kind="primary"]:hover {
        background-color: #1EBE5D !important;
        color: white !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Exibe o logo local salvo na pasta do projeto
st.image("logo.png", width=200)

st.title("🍢 Cuca Espetinhos e Lanches")

# Cardápio Completo
menu = {
    # Espetinhos Tradicionais
    "ESPETINHO DE CARNE": {
        "preco": 12.00,
        "imagem": "https://images.unsplash.com/photo-1529193591184-b1d58069ecdd?w=500",
        "categoria": "Espetinhos Tradicionais",
    },
    "ESPETINHO DE FRANGO": {
        "preco": 10.00,
        "imagem": "https://images.unsplash.com/photo-1532550907401-a500c9a57435?w=500",
        "categoria": "Espetinhos Tradicionais",
    },
    "ESPETINHO DE LINGUIÇA": {
        "preco": 10.00,
        "imagem": "https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=500",
        "categoria": "Espetinhos Tradicionais",
    },
    "ESPETINHO DE QUEIJO COALHO": {
        "preco": 11.00,
        "imagem": "https://images.unsplash.com/photo-1599488615731-7e5c2823ff28?w=500",
        "categoria": "Espetinhos Tradicionais",
    },
    "ESPETINHO DE CORAÇÃO": {
        "preco": 12.00,
        "imagem": "https://images.unsplash.com/photo-1544025162-d76694265947?w=500",
        "categoria": "Espetinhos Tradicionais",
    },
    "ESPETINHO DE KAFTA": {
        "preco": 12.00,
        "imagem": "https://images.unsplash.com/photo-1529193591184-b1d58069ecdd?w=500",
        "categoria": "Espetinhos Tradicionais",
    },
    # Espetinhos Especiais
    "ESPETINHO DE MEDALHÃO DE FRANGO": {
        "preco": 14.00,
        "imagem": "https://images.unsplash.com/photo-1532550907401-a500c9a57435?w=500",
        "categoria": "Espetinhos Especiais",
    },
    "ESPETINHO DE MEDALHÃO DE CARNE": {
        "preco": 15.00,
        "imagem": "https://images.unsplash.com/photo-1529193591184-b1d58069ecdd?w=500",
        "categoria": "Espetinhos Especiais",
    },
    "ESPETINHO DE PÃO DE ALHO": {
        "preco": 9.00,
        "imagem": "https://images.unsplash.com/photo-1573140247632-f8fd74997d5c?w=500",
        "categoria": "Espetinhos Especiais",
    },
    "ESPETINHO DE QUEIJO COM GOIABADA": {
        "preco": 11.00,
        "imagem": "https://images.unsplash.com/photo-1599488615731-7e5c2823ff28?w=500",
        "categoria": "Espetinhos Especiais",
    },
    # Lanches
    "X BURGER": {
        "preco": 19.90,
        "imagem": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=500",
        "categoria": "Lanches",
    },
    "X SALADA": {
        "preco": 22.90,
        "imagem": "https://images.unsplash.com/photo-1550547660-d9450f859349?w=500",
        "categoria": "Lanches",
    },
    "X BACON": {
        "preco": 25.90,
        "imagem": "https://images.unsplash.com/photo-1553979459-d2229ba7433b?w=500",
        "categoria": "Lanches",
    },
    "X TUDO": {
        "preco": 29.90,
        "imagem": "https://images.unsplash.com/photo-1586190848861-99aa4a171e90?w=500",
        "categoria": "Lanches",
    },
    "LANCHE DE ESPETINHO NO PÃO": {
        "preco": 18.00,
        "imagem": "https://images.unsplash.com/photo-1627308595229-7830a5c91f9f?w=500",
        "categoria": "Lanches",
    },
    # Acompanhamentos e Porções
    "PORÇÃO DE MANDIOCA FRITA": {
        "preco": 20.00,
        "imagem": "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?w=500",
        "categoria": "Acompanhamentos e Porções",
    },
    "PORÇÃO DE BATATA FRITA": {
        "preco": 20.00,
        "imagem": "https://images.unsplash.com/photo-1576107232684-1279f3908594?w=500",
        "categoria": "Acompanhamentos e Porções",
    },
    "PORÇÃO DE BATATA COM BACON E CHEDDAR": {
        "preco": 28.00,
        "imagem": "https://images.unsplash.com/photo-1585109649139-366815a0d713?w=500",
        "categoria": "Acompanhamentos e Porções",
    },
    "FAROFA DA CASA": {
        "preco": 5.00,
        "imagem": "https://images.unsplash.com/photo-1541544741938-0af808871cc0?w=500",
        "categoria": "Acompanhamentos e Porções",
    },
    "VINAGRETE": {
        "preco": 5.00,
        "imagem": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=500",
        "categoria": "Acompanhamentos e Porções",
    },
    # Bebidas
    "REFRIGERANTE LATA": {
        "preco": 6.00,
        "imagem": "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=500",
        "categoria": "Bebidas",
    },
    "REFRIGERANTE 2L": {
        "preco": 14.00,
        "imagem": "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=500",
        "categoria": "Bebidas",
    },
    "CERVEJA LATA": {
        "preco": 7.00,
        "imagem": "https://images.unsplash.com/photo-1608270586620-248524c67de9?w=500",
        "categoria": "Bebidas",
    },
    "CERVEJA LONG NECK": {
        "preco": 10.00,
        "imagem": "https://images.unsplash.com/photo-1608270586620-248524c67de9?w=500",
        "categoria": "Bebidas",
    },
    "SUCO LATA": {
        "preco": 7.00,
        "imagem": "https://images.unsplash.com/photo-1613478223719-2ab802602423?w=500",
        "categoria": "Bebidas",
    },
    "ÁGUA MINERAL": {
        "preco": 4.00,
        "imagem": "https://images.unsplash.com/photo-1548839140-29a749e1bc4e?w=500",
        "categoria": "Bebidas",
    },
}

# Adicionais para lanches
adicionais = {
    "Bacon": 4.00,
    "Queijo": 3.00,
    "Ovo": 2.50,
    "Hambúrguer Extra": 7.00,
    "Maionese da Casa": 3.00,
}

# Inicialização do estado do carrinho no Streamlit
if "carrinho" not in st.session_state:
    st.session_state.carrinho = {}

if "adicionais_lanches" not in st.session_state:
    st.session_state.adicionais_lanches = {}

# --- MODAL DE CONFIRMAÇÃO DO PEDIDO ---
@st.dialog("📋 Confirmar e Enviar Pedido")
def modal_confirmacao(numero_wa, resumo_texto):
    st.write("### Por favor, revise os dados antes de enviar:")
    st.info(resumo_texto)

    link_whatsapp = f"https://api.whatsapp.com/send?phone={numero_wa}&text={urllib.parse.quote(resumo_texto)}"

    st.write("---")
    col_voltar, col_enviar = st.columns([1, 2])

    with col_voltar:
        if st.button("❌ Alterar Pedido", use_container_width=True):
            st.rerun()

    with col_enviar:
        st.link_button(
            "📲 CONFIRMAR E ENVIAR",
            link_whatsapp,
            type="primary",
            use_container_width=True,
        )


# --- EXIBIÇÃO DO CARDÁPIO POR CATEGORIAS ---
st.subheader("📋 Nosso Cardápio")

categorias = [
    "Espetinhos Tradicionais",
    "Espetinhos Especiais",
    "Lanches",
    "Acompanhamentos e Porções",
    "Bebidas",
]

for cat in categorias:
    st.markdown(f"### {cat}")

    for item, info in menu.items():
        if info["categoria"] == cat:
            col1, col2, col3 = st.columns([1, 2, 1])

            with col1:
                st.image(info["imagem"], use_container_width=True)

            with col2:
                st.write(f"**{item}**")
                st.write(f"R$ {info['preco']:.2f}".replace(".", ","))

                # Opção de adicionais se o item for um Lanche
                if cat == "Lanches":
                    adds_selecionados = st.multiselect(
                        f"Adicionais para {item}:",
                        options=list(adicionais.keys()),
                        format_func=lambda x: f"{x} (+R$ {adicionais[x]:.2f})".replace(
                            ".", ","
                        ),
                        key=f"add_select_{item}",
                    )
                    st.session_state.adicionais_lanches[item] = adds_selecionados

            with col3:
                if st.button("Adicionar", key=f"add_{item}"):
                    st.session_state.carrinho[item] = (
                        st.session_state.carrinho.get(item, 0) + 1
                    )
                    st.toast(f"{item} adicionado ao carrinho!", icon="🛒")
                    st.rerun()

    st.markdown("---")

# --- CARRINHO E FINALIZAÇÃO ---
st.subheader("🛒 Seu Carrinho")

if not st.session_state.carrinho:
    st.write("Seu carrinho está vazio.")
else:
    total_geral = 0.0
    resumo_itens_wa = []

    for item, qtd in list(st.session_state.carrinho.items()):
        preco_unitario = menu[item]["preco"]
        subtotal = preco_unitario * qtd

        # Calcula adicionais para Lanches
        valor_adicionais = 0.0
        lista_adds_str = ""
        adds_item = st.session_state.adicionais_lanches.get(item, [])

        if adds_item:
            for add in adds_item:
                valor_adicionais += adicionais[add]
            lista_adds_str = f" (Adicionais: {', '.join(adds_item)})"

        subtotal += valor_adicionais * qtd
        total_geral += subtotal

        col_desc, col_qtd, col_del = st.columns([2, 1, 1])

        with col_desc:
            st.write(
                f"**{item}**{lista_adds_str}\n\nR$ {preco_unitario + valor_adicionais:.2f}".replace(
                    ".", ","
                )
            )

        with col_qtd:
            st.write(f"Qtd: {qtd}")

        with col_del:
            if st.button("🗑️", key=f"rem_{item}"):
                del st.session_state.carrinho[item]
                st.rerun()

        resumo_itens_wa.append(
            f"• {qtd}x {item}{lista_adds_str} - R$ {subtotal:.2f}".replace(
                ".", ","
            )
        )

    st.divider()

    # Opções de Entrega ou Retirada
    tipo_pedido = st.radio(
        "Como deseja receber seu pedido?", ["Entrega (Delivery)", "Retirada no Balcão"]
    )

    taxa_entrega = 0.0
    if tipo_pedido == "Entrega (Delivery)":
        taxa_entrega = 5.00  # Taxa fixa de entrega de R$ 5,00
        st.info("Taxa de entrega: R$ 5,00")
        endereco = st.text_input("Endereço completo de entrega:")
        referencia = st.text_input("Ponto de referência (opcional):")
    else:
        endereco = "Retirada no Balcão"
        referencia = "N/A"

    total_geral += taxa_entrega

    st.markdown(
        f"### **Total Final: R$ {total_geral:.2f}**".replace(".", ",")
    )

    # Dados do Cliente
    st.markdown("---")
    st.subheader("👤 Dados do Cliente")
    nome_cliente = st.text_input("Seu nome:")
    pagamento = st.selectbox(
        "Forma de Pagamento:",
        ["Pix", "Cartão de Débito", "Cartão de Crédito", "Dinheiro"],
    )

    troco_para = ""
    if pagamento == "Dinheiro":
        troco_para = st.text_input(
            "Precisa de troco para quanto? (Ex: R$ 50,00):"
        )

    observacoes = st.text_area(
        "Observações do pedido (ex: tirar cebola, ponto da carne, etc):"
    )

    # Botão para abrir o diálogo/modal de confirmação
    if st.button(
        "🚀 AVANÇAR PARA CONFIRMAÇÃO", type="primary", use_container_width=True
    ):
        if not nome_cliente:
            st.error("Por favor, preencha o seu nome antes de continuar.")
        elif tipo_pedido == "Entrega (Delivery)" and not endereco:
            st.error("Por favor, preencha o endereço de entrega.")
        else:
            # Monta o texto completo para enviar via WhatsApp
            mensagem_wa = f"🍢 *NOVO PEDIDO - CUCA ESPETINHOS*\n\n"
            mensagem_wa += f"👤 *Cliente:* {nome_cliente}\n"
            mensagem_wa += f"📦 *Tipo:* {tipo_pedido}\n"

            if tipo_pedido == "Entrega (Delivery)":
                mensagem_wa += f"📍 *Endereço:* {endereco}\n"
                if referencia:
                    mensagem_wa += f"🚩 *Ref:* {referencia}\n"

            mensagem_wa += f"\n📋 *ITENS DO PEDIDO:*\n"
            mensagem_wa += "\n".join(resumo_itens_wa) + "\n\n"

            if taxa_entrega > 0:
                mensagem_wa += f"🛵 *Taxa de Entrega:* R$ {taxa_entrega:.2f}\n".replace(
                    ".", ","
                )

            mensagem_wa += f"💰 *TOTAL:* R$ {total_geral:.2f}\n".replace(
                ".", ","
            )
            mensagem_wa += f"💳 *Forma de Pagamento:* {pagamento}\n"

            if troco_para:
                mensagem_wa += f"💵 *Troco para:* {troco_para}\n"

            if observacoes:
                mensagem_wa += f"📝 *Obs:* {observacoes}\n"

            # Número de telefone do estabelecimento (com DDD e DDI 55)
            NUMERO_WHATSAPP = "5512999999999"  # <--- Altere para o seu número real

            # Abre o modal de confirmação antes de redirecionar para o WhatsApp
            modal_confirmacao(NUMERO_WHATSAPP, mensagem_wa)
