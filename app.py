import urllib.parse
import streamlit as st

st.set_page_config(
    page_title="Cuca Espetinhos e Lanches", page_icon="🍢", layout="centered"
)

# Estilo para formatar o cupom térmico na tela
st.markdown(
    """
    <style>
    @media print {
        body * { visibility: hidden; }
        .cupom-termico, .cupom-termico * { visibility: visible; }
        .cupom-termico { position: absolute; left: 0; top: 0; width: 100%; }
    }
    .cupom-termico {
        background-color: #fff;
        color: #000;
        font-family: 'Courier New', Courier, monospace;
        padding: 15px;
        border: 1px dashed #000;
        width: 300px;
        margin: 10px auto;
        font-size: 13px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

st.title("🍢 Cuca Espetinhos e Lanches")

# Cardápio
menu = {
    "Espetinho de Carne": {
        "preco": 10.00,
        "imagem": "https://images.unsplash.com/photo-1529193591184-b1d58069ecdd?w=400",
    },
    "Espetinho de Frango": {
        "preco": 9.00,
        "imagem": "https://images.unsplash.com/photo-1598515214211-89d3c73ae83b?w=400",
    },
    "Espetinho de Linguiça": {
        "preco": 9.00,
        "imagem": "https://images.unsplash.com/photo-1544025162-d76694265947?w=400",
    },
    "X-Burguer": {
        "preco": 15.00,
        "imagem": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400",
    },
    "Refrigerante Lata": {
        "preco": 6.00,
        "imagem": "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=400",
    },
}

carrinho = []
total = 0.0

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
            subtotal = info["preco"] * qtd
            carrinho.append(
                {"item": item, "qtd": qtd, "subtotal": subtotal}
            )
            total += subtotal

if carrinho:
    st.divider()
    st.write(f"### Total: R$ {total:.2f}")

    nome = st.text_input("Seu Nome:")
    endereco = st.text_input("Endereço de Entrega:")
    pagamento = st.selectbox(
        "Forma de Pagamento", ["Pix", "Cartão", "Dinheiro"]
    )

    if nome and endereco:
        # Formatação do texto para o WhatsApp
        itens_txt = "\n".join(
            [f"{i['qtd']}x {i['item']} (R$ {i['subtotal']:.2f})" for i in carrinho]
        )
        mensagem = (
            f"Olá! Gostaria de fazer um pedido na *Cuca Espetinhos e Lanches*:\n\n"
            f"*Cliente:* {nome}\n"
            f"*Endereço:* {endereco}\n"
            f"*Pagamento:* {pagamento}\n\n"
            f"*Itens:*\n{itens_txt}\n\n"
            f"*Total:* R$ {total:.2f}"
        )

        numero_whatsapp = "5511999999999"  # Substitua pelo número real
        link = f"https://wa.me/{numero_whatsapp}?text={urllib.parse.quote(mensagem)}"

        st.markdown(
            f"[👉 Clique aqui para enviar o pedido no WhatsApp]({link})",
            unsafe_allow_html=True,
        )

        # Visualização do Cupom Térmico para Impressão
        st.divider()
        st.subheader("📄 Comanda do Pedido")

        # HTML formatado estilo cupom de impressora térmica (58mm/80mm)
        itens_html = "".join(
            [
                f"<tr><td>{i['qtd']}x {i['item']}</td><td style='text-align:right;'>R$ {i['subtotal']:.2f}</td></tr>"
                for i in carrinho
            ]
        )

        cupom_html = f"""
        <div class="cupom-termico">
            <h3 style="text-align:center; margin:0;">CUCA ESPETINHOS</h3>
            <p style="text-align:center; margin:0;">--------------------------------</p>
            <p><b>CLIENTE:</b> {nome}<br>
            <b>ENDEREÇO:</b> {endereco}<br>
            <b>PAGTO:</b> {pagamento}</p>
            <p style="text-align:center; margin:0;">--------------------------------</p>
            <table style="width:100%; font-size:12px;">
                {itens_html}
            </table>
            <p style="text-align:center; margin:0;">--------------------------------</p>
            <h4 style="text-align:right; margin:5px 0;">TOTAL: R$ {total:.2f}</h4>
        </div>
        """

        st.markdown(cupom_html, unsafe_allow_html=True)

        # Botão acionando o comando de impressão do próprio navegador
        st.components.v1.html(
            """
            <button onclick="window.print()" style="
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                width: 100%;
                font-size: 16px;">
                🖨️ Imprimir Comanda na Impressora Térmica
            </button>
            """,
            height=50,
        )