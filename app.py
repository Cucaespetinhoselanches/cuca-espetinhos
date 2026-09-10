import urllib.parse
import streamlit as st
import streamlit.components.v1 as components  # Import para rodar o JavaScript

# ==================== ESTADOS DA SESSÃO ====================
if "mostrar_modal" not in st.session_state:
    st.session_state["mostrar_modal"] = False

if "etapa_pedido" not in st.session_state:
    st.session_state["etapa_pedido"] = "cardapio"

if "ultimo_item_alterado" not in st.session_state:
    st.session_state["ultimo_item_alterado"] = None

# Callback Functions
def registrar_alteracao_item(nome_item):
    if st.session_state.get(nome_item, 0) > 0:
        st.session_state["ultimo_item_alterado"] = nome_item

def avancar_para_entrega():
    st.session_state["etapa_pedido"] = "dados_entrega"

def continuar_comprando():
    st.session_state["ultimo_item_alterado"] = None
    st.session_state["etapa_pedido"] = "cardapio"

# ==================== MODAL DE CONFIRMAÇÃO ====================
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

# Estilização CSS
st.markdown(
    """
    <style>
    label, div[data-testid="stMarkdownContainer"] p {
        font-size: 18px !important;
    }

    h1 { font-size: 32px !important; }
    h2 { font-size: 26px !important; }
    h3 { font-size: 22px !important; }

    .preco-destaque {
        font-size: 20px !important;
        font-weight: bold !important;
        color: #2e7d32 !important;
    }

    div.stButton > button {
        font-size: 18px !important;
        font-weight: bold !important;
        min-height: 3em !important;
        border-radius: 10px !important;
    }

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
    "PORÇÃO BATATA FRITA ou PORÇÃO DE MANDIOCA FRITA": {
        "preco": 29.90,
        "imagem": "https://plus.unsplash.com/premium_photo-1672774750509-bc9ff226f3e8?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8cG9yJUMzJUE3JUMzJUE3byUyMGJhdGF0YSUyMGZyaXRhfGVufDB8fDB8fHww",
    },
    "PORÇÃO ANÉIS DE CEBOLA": {
        "preco": 28.90,
        "imagem": "https://images.unsplash.com/photo-1766589152292-3c052f0d87aa?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fHBvciVDMyVBNyVDMyVBM28lMjBhbmVpcyUyMGRlJTIwY2Vib2xhfGVufDB8fDB8fHww",
    },
    "PORÇÃO COMBO DE PORÇÕES": {
        "preco": 49.90,
        "imagem": "https://images.unsplash.com/photo-1702827495434-629df15aa136?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDB8fHBvciVDMyVBNyVDMyVBM28lMjBjb21ib3xlbnwwfHwwfHx8MA%3D%3D",
    },
    "ESPETO PÃO DE ALHO ou QUEIJO COALHO ou LINGUIÇA": {
        "preco": 9.00,
        "imagem": "https://i.pinimg.com/474x/ca/88/97/ca8897789a429b07bc7a9f238c348223.jpg",
    },
    "ESPETO ROMEU E JULIETA (Bacon/Goiabada/Queijo)": {
        "preco": 15.00,
        "imagem": "https://media.istockphoto.com/id/1270859209/pt/foto/kebab-grilled-meat-on-a-cutting-board-with-flour-and-vinaigrette-salad.jpg?s=612x612&w=0&k=20&c=K50axpMgL8NejcoLFl_HV8RI5hIKOgjPJ7AKqSsFcAk=",
    },
    "ESPETO PANCETA ou ALCATRA ou FRALDINHA ou KAFTA ou FRANGO": {
        "preco": 12.00,
        "imagem": "https://media.istockphoto.com/id/1270859209/pt/foto/kebab-grilled-meat-on-a-cutting-board-with-flour-and-vinaigrette-salad.jpg?s=612x612&w=0&k=20&c=K50axpMgL8NejcoLFl_HV8RI5hIKOgjPJ7AKqSsFcAk=",
    },
    "ESPETO PICANHA ou CORAÇÃO": {
        "preco": 18.00,
        "imagem": "https://media.istockphoto.com/id/1270859209/pt/foto/kebab-grilled-meat-on-a-cutting-board-with-flour-and-vinaigrette-salad.jpg?s=612x612&w=0&k=20&c=K50axpMgL8NejcoLFl_HV8RI5hIKOgjPJ7AKqSsFcAk=",
    },
    "Refrigerante Lata": {
        "preco": 6.00,
        "imagem": "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=400",
    },
    "Suco Del Valle 200ml": {
        "preco": 8.00,
        "imagem": "https://m.media-amazon.com/images/I/51Z3PJFvmaL._AC_UF350,350_QL80_.jpg",
    },
    "Suco 1L": {
        "preco": 10.00,
        "imagem": "https://cdn.awsli.com.br/800x800/1345/1345272/produto/55987814/01943f4345.jpg",
    },
    "Cerveja Original ou Budweiser  300ml Garrafinha": {
        "preco": 6.00,
        "imagem": "https://th.bing.com/th/id/OIP.yv46CREzjTxIfnQpp9lU5wHaHa?w=184&h=187&c=7&r=0&o=7&pid=1.7&rm=3",
    },
    "Cerveja Antarctica ou BRAHMA ou IMPERIO 300ml Garrafinha": {
        "preco": 5.00,
        "imagem": "https://th.bing.com/th/id/OIP.yv46CREzjTxIfnQpp9lU5wHaHa?w=184&h=187&c=7&r=0&o=7&pid=1.7&rm=3",
    },
    "Cerveja Skol ou AMSTEL ou IMPERIO 269ml Lata": {
        "preco": 5.00,
        "imagem": "https://tse4.mm.bing.net/th/id/OIP.Cqa-Rx_ea-YoraLE7dVVpQHaFj?r=0&pid=ImgDet&w=204&h=153&c=7&o=7&rm=3",
    },
    "Cerveja Budweiser ou ORIGINAL oU Brahma Duplo Malte 269ml Lata": {
        "preco": 6.00,
        "imagem": "https://tse4.mm.bing.net/th/id/OIP.Cqa-Rx_ea-YoraLE7dVVpQHaFj?r=0&pid=ImgDet&w=204&h=153&c=7&o=7&rm=3",
    },
    "Cerveja Long Neck Heineken ou Budweiser ou CORONA": {
        "preco": 10.00,
        "imagem": "https://images.unsplash.com/photo-1618885472179-5e474019f2a9?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8Z2FycmFmYSUyMGRlJTIwY2VydmVqYXxlbnwwfHwwfHx8MA%3D%3D",
    },
    "Energético Monster 473ml": {
        "preco": 14.00,
        "imagem": "https://thumb.wikimedia.org/wikipedia/commons/thumb/0/06/Monster_Energy_drink_%28cropped%29.jpg/960px-Monster_Energy_drink_%28cropped%29.jpg?utm_source=en.wikipedia.org&utm_campaign=index&utm_content=thumbnail",
    },
    "Cerveja Amstel ou IMPERIO 350ml Lata": {
        "preco": 6.00,
        "imagem": "https://tse4.mm.bing.net/th/id/OIP.Cqa-Rx_ea-YoraLE7dVVpQHaFj?r=0&pid=ImgDet&w=204&h=153&c=7&o=7&rm=3",
    },
    "Cerveja Brahma Duplo Malte 350ml Lata": {
        "preco": 7.00,
        "imagem": "https://tse4.mm.bing.net/th/id/OIP.Cqa-Rx_ea-YoraLE7dVVpQHaFj?r=0&pid=ImgDet&w=204&h=153&c=7&o=7&rm=3",
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
            on_change=registrar_alteracao_item,
            args=(item,),
        )
        if qtd > 0:
            subtotal_item = info["preco"] * qtd
            carrinho.append(
                {"item": item, "qtd": qtd, "subtotal": subtotal_item}
            )
            subtotal_produtos += subtotal_item

    # Pergunta exibida logo abaixo do item selecionado
    if (
        st.session_state.get("ultimo_item_alterado") == item
        and qtd > 0
        and st.session_state["etapa_pedido"] == "cardapio"
    ):
        st.info(f"✅ **{qtd}x {item}** adicionado ao pedido!")
        st.markdown("**Deseja inserir mais produtos ou encerrar o pedido?**")

        col_mais, col_encerrar = st.columns(2)
        with col_mais:
            st.button(
                "➕ Inserir mais produtos",
                key=f"btn_mais_{item}",
                use_container_width=True,
                on_click=continuar_comprando,
            )

        with col_encerrar:
            st.button(
                "✅ Encerrar pedido",
                key=f"btn_encerrar_{item}",
                type="primary",
                use_container_width=True,
                on_click=avancar_para_entrega,
            )

        st.write("---")

# ==================== DADOS DE ENTREGA E PAGAMENTO ====================
if carrinho and st.session_state["etapa_pedido"] == "dados_entrega":
    # ÂNCORA PARA A ROLAGEM AUTOMÁTICA
    st.markdown("<div id='secao-entrega'></div>", unsafe_allow_html=True)

    st.divider()
    st.subheader("📦 Dados de Entrega e Pagamento")
    st.write(f"### **Subtotal dos itens: R$ {subtotal_produtos:.2f}**")

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

    # JAVASCRIPT: Executa o rolamento automático suave para a seção de entrega
    components.html(
        """
        <script>
            var elemento = window.parent.document.getElementById('secao-entrega');
            if (elemento) {
                elemento.scrollIntoView({behavior: 'smooth'});
            }
        </script>
        """,
        height=0,
    )
