'use client';

import React, { useState } from 'react';
import { ShoppingBag, Plus, Minus, Check, ArrowLeft, Send } from 'lucide-react';

const WHATSAPP_NUMBER = process.env.NEXT_PUBLIC_WHATSAPP_NUMBER || "5512992093751";
const CHAVE_PIX_VAL = process.env.NEXT_PUBLIC_CHAVE_PIX || "19919105848";

const menuCategorias = {
  "🍢 Espetos": [
    { name: "ESPETO PÃO DE ALHO", price: 9.00, image: "https://casadecarnesdomaninho.com.br/wp-content/uploads/2022/06/espetinho-pao-de-alho.jpg" },
    { name: "ESPETO ROMEU E JULIETA (Bacon/Goiabada/Queijo)", price: 15.00, image: "https://content.paodeacucar.com/wp-content/uploads/2017/06/espetinhos-carne-churrasco-festa-junina1.jpg" },
    { name: "ESPETO QUEIJO COALHO", price: 9.00, image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpyXQSm25u3do9kGas7sKk1Lf1oXX7mcrS5IC9w5UPKUfGRAdrjq2a8vFs&s=10" },
    { name: "ESPETO PANCETA", price: 12.00, image: "https://content.paodeacucar.com/wp-content/uploads/2017/06/espetinhos-carne-churrasco-festa-junina1.jpg" },
    { name: "ESPETO ALCATRA", price: 12.00, image: "https://content.paodeacucar.com/wp-content/uploads/2017/06/espetinhos-carne-churrasco-festa-junina1.jpg" },
    { name: "ESPETO PICANHA", price: 18.00, image: "https://content.paodeacucar.com/wp-content/uploads/2017/06/espetinhos-carne-churrasco-festa-junina1.jpg" },
    { name: "ESPETO FRALDINHA", price: 12.00, image: "https://content.paodeacucar.com/wp-content/uploads/2017/06/espetinhos-carne-churrasco-festa-junina1.jpg" },
    { name: "ESPETO LINGUIÇA", price: 9.00, image: "https://content.paodeacucar.com/wp-content/uploads/2017/06/espetinhos-carne-churrasco-festa-junina1.jpg" },
    { name: "ESPETO LINGUIÇA GOURMET", price: 9.00, image: "https://content.paodeacucar.com/wp-content/uploads/2017/06/espetinhos-carne-churrasco-festa-junina1.jpg" },
    { name: "ESPETO KAFTA", price: 12.00, image: "https://content.paodeacucar.com/wp-content/uploads/2017/06/espetinhos-carne-churrasco-festa-junina1.jpg" },
    { name: "ESPETO KAFTA GOURMET", price: 14.00, image: "https://content.paodeacucar.com/wp-content/uploads/2017/06/espetinhos-carne-churrasco-festa-junina1.jpg" },
    { name: "ESPETO CORAÇÃO", price: 18.00, image: "https://content.paodeacucar.com/wp-content/uploads/2017/06/espetinhos-carne-churrasco-festa-junina1.jpg" },
    { name: "ESPETO FRANGO", price: 12.00, image: "https://content.paodeacucar.com/wp-content/uploads/2017/06/espetinhos-carne-churrasco-festa-junina1.jpg" }
  ],
  "🥪 Lanches": [
    { name: "X BURGER", price: 19.90, image: "https://plus.unsplash.com/premium_photo-1675252369719-dd52bc69c3df?w=800&auto=format&fit=crop&q=60" },
    { name: "X SALADA", price: 29.90, image: "https://plus.unsplash.com/premium_photo-1675252369719-dd52bc69c3df?w=800&auto=format&fit=crop&q=60" },
    { name: "X BACON", price: 35.90, image: "https://plus.unsplash.com/premium_photo-1675252369719-dd52bc69c3df?w=800&auto=format&fit=crop&q=60" },
    { name: "X-EGG", price: 30.90, image: "https://plus.unsplash.com/premium_photo-1675252369719-dd52bc69c3df?w=800&auto=format&fit=crop&q=60" },
    { name: "X-CATUPIRY EMPANADO", price: 32.90, image: "https://plus.unsplash.com/premium_photo-1675252369719-dd52bc69c3df?w=800&auto=format&fit=crop&q=60" },
    { name: "FRANGÃO", price: 32.90, image: "https://plus.unsplash.com/premium_photo-1675252369719-dd52bc69c3df?w=800&auto=format&fit=crop&q=60" },
    { name: "HOT CALABRESA", price: 16.50, image: "https://images.unsplash.com/photo-1613482084286-41f25b486fa2?w=500&auto=format&fit=crop&q=60" },
    { name: "HOT BACON", price: 16.50, image: "https://images.unsplash.com/photo-1613482084286-41f25b486fa2?w=500&auto=format&fit=crop&q=60" },
    { name: "HOT SALADA", price: 12.50, image: "https://images.unsplash.com/photo-1613482084286-41f25b486fa2?w=500&auto=format&fit=crop&q=60" },
    { name: "HOT PURE", price: 14.50, image: "https://images.unsplash.com/photo-1613482084286-41f25b486fa2?w=500&auto=format&fit=crop&q=60" }
  ],
  "🍟 Porções": [
    { name: "PORÇÃO BATATA FRITA", price: 29.90, image: "https://2.bp.blogspot.com/-zNkU0qa51Uk/U5elL6RgI6I/AAAAAAAAACo/OngayLy9ogk/s1600/batata.jpg" },
    { name: "PORÇÃO MANDIOCA FRITA", price: 29.90, image: "https://media.istockphoto.com/id/903103922/pt/foto/brazilian-food-mandioca-frita-deep-fried-cassava-root.webp?a=1&b=1&s=612x612&w=0&k=20&c=KwVZFUrGJlRkXM6_nyBNPt_6sbpHJ1x0pR49fA2wIgY=" },
    { name: "PORÇÃO ANÉIS DE CEBOLA", price: 28.90, image: "https://images.unsplash.com/photo-1766589152292-3c052f0d87aa?w=500&auto=format&fit=crop&q=60" },
    { name: "PORÇÃO COMBO DE PORÇÕES", price: 49.90, image: "https://images.unsplash.com/photo-1702827495434-629df15aa136?w=500&auto=format&fit=crop&q=60" }
  ],
  "🥤 Refrigerantes": [
    { name: "Refrigerante COCA NORMAL Lata 350ml", price: 6.00, image: "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=400" },
    { name: "Refrigerante COCA ZERO Lata 350ml", price: 6.00, image: "https://acdn-us.mitiendanube.com/stores/001/165/503/products/coca-zero21-16e7cba0588363da7616192142363168-1024-1024.webp" },
    { name: "Refrigerante FANTA LARANJA Lata 350ml", price: 6.00, image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCj-iJ_ziGZMurwiupsfzkhhmuRr4vDxjEM4V3QapNpg&s=10" },
    { name: "Refrigerante SPRITE Lata 350ml", price: 6.00, image: "https://www.drogariaminasbrasil.com.br/media/webp/catalog/product/cache/74c1057f7991b4edb2bc7bdaa94de933/image/228324e3d/refrigerante-sprite-lata-350ml_jpg.webp" },
    { name: "Refrigerante FANTA UVA Lata 350ml", price: 6.00, image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQy8MfxKAF9fZHoP5jOkB_GVC3llWVFJgX8bqaQQsBNTw&s=10" },
    { name: "Refrigerante GUARANA ANTARCTICA Lata 350ml", price: 6.00, image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRo_of1b4lkVoGXo7VNDcQ2zcyItH2BvZ-A2XFU362rbA&s=10" },
    { name: "Refrigerante TONICA SCHWEPPES Lata 350ml", price: 6.50, image: "https://www.imigrantesbebidas.com.br/bebida/images/products/full/2209-agua-tonica-schweppes-lata-350ml.jpg" },
    { name: "Refrigerante FANTA LARANJA Garrafinha 200ml", price: 3.50, image: "https://mercantilatacado.vtexassets.com/arquivos/ids/172941/654a33c475d9096810e2cbfc.jpg?v=638349585366670000" },
    { name: "Refrigerante COCA COLA Garrafinha 200ml", price: 3.50, image: "https://mercantilnovaera.vtexassets.com/arquivos/ids/181329/Refrigerante-COCA-COLA-Garrafa-Pet-200ml.jpg?v=637602425279600000" },
    { name: "Refrigerante COCA ZERO Garrafinha 200ml", price: 3.50, image: "https://prezunic.vtexassets.com/arquivos/ids/210276-800-auto?v=638568370331100000" },
    { name: "Refrigerante GUARANITA Garrafinha 200ml", price: 3.50, image: "https://phygital-files.mercafacil.com/fernandes-bucket/uploads/produto/cibal_guaranita_200ml_4762cf0e-e46e-4cb8-b0cf-5e3c11785572.jpg" },
    { name: "Refrigerante SPRITE Garrafinha 200ml", price: 3.50, image: "https://mercantilnovaera.vtexassets.com/arquivos/ids/170425/Refrigerante-Limao-Sprite-Garrafa-200ml.jpg?v=637442546240970000" },
    { name: "Refrigerante COCA COLA 2L", price: 17.00, image: "https://gbarbosa.vtexassets.com/arquivos/ids/214289/655268ba8d0743e14888f712.jpg?v=638354963814100000" },
    { name: "Refrigerante PEPSI 2L", price: 17.00, image: "https://hiperideal.vtexassets.com/arquivos/ids/228374/7892840800000-RefrigerantePEPSIGarrafa2L-1.jpg?v=638733302785230000" },
    { name: "Refrigerante COCA ZERO 2.5L", price: 17.00, image: "https://mercantilnovaera.vtexassets.com/arquivos/ids/230310/45911-1779911965249.png.png?v=639155088729770000" },
    { name: "Refrigerante COCA ZERO 1L", price: 10.00, image: "https://mercantilatacado.vtexassets.com/arquivos/ids/168646/653fe3aa752720c144887a35.jpg?v=638342826762370000" },
    { name: "Refrigerante H20 500ml", price: 8.00, image: "https://savegnagoio.vtexassets.com/arquivos/ids/447261-800-800?v=638525058304970000" },
    { name: "Refrigerante TONICA SCHWEPPES 600ml", price: 8.00, image: "https://almacenestampico.com/wp-content/uploads/2023/03/Almacenes-Tampico-Uruguay-agua-tonica-schwepps-600Mesa-de-trabajo-1.jpg" },
    { name: "Refrigerante FANTA UVA 600ml", price: 8.00, image: "https://io.convertiez.com.br/m/farmaciasaopaulo/shop/products/images/16728/medium/fanta-uva-600ml_25847.jpg" },
    { name: "Refrigerante SPRITE 600ml", price: 8.00, image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTxBTxJckfXC_FK2APRFPRLnVY8tC68jlixc3fnLgPZAg&s" },
    { name: "Refrigerante GUARANITA 600ml", price: 8.00, image: "https://tauste.com.br/media/catalog/product/cache/207e23213cf636ccdef205098cf3c8a3/1/5/1584431777359902.jpg" },
    { name: "Refrigerante COCA COLA 600ml", price: 8.00, image: "https://bretas.vtexassets.com/arquivos/ids/182991-800-auto?v=638375498920300000" },
    { name: "Refrigerante COCA COLA ZERO 600ml", price: 8.00, image: "https://mercantilnovaera.vtexassets.com/arquivos/ids/232442/Refrigerante-COCA-COLA-Zero-Acucar-Pet-600ml.jpg?v=639179091417330000" },
    { name: "Refrigerante FANTA 600ml", price: 8.00, image: "https://phygital-files.mercafacil.com/miliozzi/uploads/produto/refrigerante_fanta_laranja_600ml_pet_a8b5c222-e21b-480c-8288-90e22dbb20d7.jpg" },
    { name: "AGUA MINERAL SEM GAS 500ml", price: 3.00, image: "https://io.convertiez.com.br/m/farmaponte/shop/products/images/22004/medium/agua-mineral-crystal-sem-gas-garrafa-1-unidade-com-500ml_17652.webp" },
    { name: "AGUA MINERAL COM GAS 500ml", price: 4.00, image: "https://apoioentrega.vteximg.com.br/arquivos/ids/1911515/139272_0.png?v=639213665179000000" }
  ],
  "🍺 Cervejas": [
    { name: "Cerveja Original 300ml Garrafinha", price: 6.00, image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRllDI7RJyBsZMII0SR2UZhiYstauUqjyhKbGznH27HEw&s=10" },
    { name: "Cerveja Budweiser 300ml Garrafinha", price: 6.00, image: "https://phygital-files.mercafacil.com/comercial-catanio-supermercado/uploads/produto/cerveja_budweiser_garrafinha_300ml_61022027-0c5d-4d8b-9f9f-620188027143.jpg" },
    { name: "Cerveja Antarctica 300ml Garrafinha", price: 5.00, image: "https://nunesbebidas.com.br/wp-content/uploads/2021/05/Nunes-Bebidas-CERVEJA-ANTARTICA-BOA-GARRAFA-300ML.jpg" },
    { name: "Cerveja Brahma 300ml Garrafinha", price: 5.00, image: "https://assets.ibecom.com.br/ib.item.image.large/l-27778dbad9724b6fb9695e6315f029e1.jpeg" },
    { name: "Cerveja Império 300ml Garrafinha", price: 5.00, image: "https://assets.ibecom.com.br/ib.item.image.large/l-ab81028dfcae4433a707b191cbe67d8c.jpeg" },
    { name: "Cerveja Skol 269ml Lata", price: 5.00, image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSSWuMoEZy8_ZGbuqI12QrAUkAjTrwh2VPt6KqEXh8CR6pzKGxtSKXBlQfz&s=10" },
    { name: "Cerveja Budweiser 269ml Lata", price: 6.00, image: "https://mambodelivery.vtexassets.com/arquivos/ids/212124-800-450?v=638537266038970000" },
    { name: "Cerveja Original 269ml Lata", price: 6.00, image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsK7x1diT-koyfCAdWSUBoHZTgPloiJYMjbRSfxGJzaw&s=10" },
    { name: "Cerveja Amstel 269ml Lata", price: 5.00, image: "https://m.media-amazon.com/images/I/61gLfj5ExrL._AC_UF1000,1000_QL80_.jpg" },
    { name: "Cerveja Império 269ml Lata", price: 5.00, image: "https://bretas.vtexassets.com/arquivos/ids/202744-800-auto?v=638376354703200000" },
    { name: "Cerveja Brahma Duplo Malte 269ml Lata", price: 6.00, image: "https://a-static.mlcdn.com.br/420x420/cerveja-brahma-duplo-malte-lager-15-unidades-lata-269ml/jrr/0f7b0dc65aa911ecb4ca4201ac18503a/3faba7ce5a536589f67a76512b5cbf98.jpg" },
    { name: "Cerveja Long Neck Heineken", price: 10.00, image: "https://images.unsplash.com/photo-1618885472179-5e474019f2a9?w=500&auto=format&fit=crop&q=60" },
    { name: "Cerveja Long Neck Budweiser", price: 10.00, image: "https://images.unsplash.com/photo-1587669284207-e8ee0fc74144?w=500&auto=format&fit=crop&q=60" },
    { name: "Cerveja Long Neck Corona", price: 10.00, image: "https://images.unsplash.com/photo-1600213903598-25be92abde40?w=500&auto=format&fit=crop&q=60" },
    { name: "Energético Monster 473ml", price: 14.00, image: "https://andinacocacola.vtexassets.com/arquivos/ids/158541/112666_COCA---MONSTER_GREEN__LT_473ML.jpg?v=639238910718900000" },
    { name: "Cerveja Amstel 350ml Lata", price: 6.00, image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRqQ_3JZ9bzr9LODFFj1Lps0OroT6jJ_PrC24CiZ0nEHg&s=10" },
    { name: "Cerveja Império 350ml Lata", price: 6.00, image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXKTXeRvTYQBjWEX-eei2xutbAx97LRhZnpOrEEQ_5Dg&s=10" },
    { name: "Cerveja Brahma Duplo Malte 350ml Lata", price: 7.00, image: "https://hortifrutibr.vtexassets.com/arquivos/ids/173202/Cerveja-Brahma-Duplo-Malte-Lata-Sleek-350Ml.png?v=639239767332900000" }
  ]
};

const taxasBairros = {
  "Nova Jacareí": 3.00,
  "Igarapés": 5.00,
  "Esperança": 4.00,
  "Centro": 8.00,
  "Outro Bairro (A combinar)": 0.00
};

export default function App() {
  const [categoriaAtiva, setCategoriaAtiva] = useState(Object.keys(menuCategorias)[0]);
  const [carrinho, setCarrinho] = useState({});
  const [etapa, setEtapa] = useState('cardapio'); // 'cardapio' | 'checkout'
  
  // Form checkout
  const [nome, setNome] = useState('');
  const [tipoEntrega, setTipoEntrega] = useState('Entrega');
  const [bairro, setBairro] = useState(Object.keys(taxasBairros)[0]);
  const [ruaNumero, setRuaNumero] = useState('');
  const [formaPagamento, setFormaPagamento] = useState('Pix');

  const alterarQtd = (nomeItem, preco, delta) => {
    setCarrinho((prev) => {
      const atual = prev[nomeItem] ? prev[nomeItem].qtd : 0;
      const novaQtd = Math.max(0, atual + delta);
      
      if (novaQtd === 0) {
        const copy = { ...prev };
        delete copy[nomeItem];
        return copy;
      }

      return {
        ...prev,
        [nomeItem]: { name: nomeItem, price: preco, qtd: novaQtd, subtotal: novaQtd * preco }
      };
    });
  };

  const itensCarrinho = Object.values(carrinho);
  const totalItens = itensCarrinho.reduce((acc, item) => acc + item.qtd, 0);
  const subtotalProdutos = itensCarrinho.reduce((acc, item) => acc + item.subtotal, 0);
  const taxaEntrega = tipoEntrega === 'Entrega' ? taxasBairros[bairro] || 0 : 0;
  const totalFinal = subtotalProdutos + taxaEntrega;

  const enviarWhatsApp = () => {
    if (!nome.trim()) return alert("Por favor, preencha o seu nome.");
    if (tipoEntrega === 'Entrega' && !ruaNumero.trim()) return alert("Por favor, preencha a Rua e Número.");

    let textoItens = itensCarrinho.map(i => `${i.qtd}x ${i.name} (R$ ${i.subtotal.toFixed(2)})`).join("\n");
    let detalhesEntrega = tipoEntrega === 'Entrega' 
      ? `*Tipo:* Entrega\n*Endereço:* ${ruaNumero} - ${bairro}\n*Taxa:* R$ ${taxaEntrega.toFixed(2)}`
      : `*Tipo:* Retirada no Local`;
    
    let pagamentoTxt = formaPagamento === 'Pix' ? `Pix (Chave: ${CHAVE_PIX_VAL})` : formaPagamento;

    let mensagem = `Olá! Gostaria de fazer um pedido na *Cuca Espetinhos e Lanches*:\n\n` +
      `*Cliente:* ${nome}\n` +
      `${detalhesEntrega}\n` +
      `*Pagamento:* ${pagamentoTxt}\n\n` +
      `*Itens:*\n${textoItens}\n\n` +
      `*Total a Pagar:* R$ ${totalFinal.toFixed(2)}`;

    window.open(`https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(mensagem)}`, '_blank');
  };

  return (
    <div className="min-h-screen bg-slate-900 text-slate-100 pb-28">
      {/* Cabeçalho */}
      <header className="sticky top-0 z-20 bg-slate-900/95 backdrop-blur border-b border-slate-800 p-4 text-center">
        <h1 className="text-2xl font-black text-red-500">🍢 Cuca Espetinhos e Lanches</h1>
        <p className="text-sm text-slate-400">Monte seu pedido de forma rápida e prática</p>
      </header>

      {etapa === 'cardapio' ? (
        <main className="max-w-xl mx-auto px-4 pt-4">
          {/* Categorias (Navegação Horizontal) */}
          <div className="flex overflow-x-auto gap-2 py-2 mb-4 scrollbar-none">
            {Object.keys(menuCategorias).map((cat) => (
              <button
                key={cat}
                onClick={() => setCategoriaAtiva(cat)}
                className={`px-4 py-2 rounded-xl text-sm font-bold whitespace-nowrap transition-all ${
                  categoriaAtiva === cat
                    ? 'bg-red-500 text-white shadow-lg shadow-red-500/30'
                    : 'bg-slate-800 text-slate-400 border border-slate-700'
                }`}
              >
                {cat}
              </button>
            ))}
          </div>

          {/* Lista de Produtos */}
          <div className="space-y-3">
            {menuCategorias[categoriaAtiva].map((item) => {
              const qtd = carrinho[item.name]?.qtd || 0;
              return (
                <div key={item.name} className="flex gap-4 p-3 bg-slate-800/80 border border-slate-700/60 rounded-2xl items-center shadow-md">
                  <img src={item.image} alt={item.name} className="w-20 h-20 object-cover rounded-xl bg-slate-900" />
                  <div className="flex-1 min-w-0">
                    <h3 className="font-bold text-sm leading-snug line-clamp-2">{item.name}</h3>
                    <span className="inline-block mt-1 px-2.5 py-0.5 bg-green-700 text-white font-black text-sm rounded-md">
                      R$ {item.price.toFixed(2)}
                    </span>
                  </div>

                  {/* Controle de Quantidade estilo App */}
                  <div className="flex items-center gap-2 bg-slate-900 border border-slate-700 rounded-xl p-1">
                    {qtd > 0 && (
                      <>
                        <button
                          onClick={() => alterarQtd(item.name, item.price, -1)}
                          className="w-7 h-7 flex items-center justify-center bg-slate-800 hover:bg-slate-700 text-white rounded-lg active:scale-95"
                        >
                          <Minus size={14} />
                        </button>
                        <span className="font-bold text-sm w-4 text-center">{qtd}</span>
                      </>
                    )}
                    <button
                      onClick={() => alterarQtd(item.name, item.price, 1)}
                      className="w-7 h-7 flex items-center justify-center bg-red-500 hover:bg-red-600 text-white rounded-lg active:scale-95"
                    >
                      <Plus size={14} />
                    </button>
                  </div>
                </div>
              );
            })}
          </div>
        </main>
      ) : (
        /* Tela de Checkout */
        <main className="max-w-xl mx-auto px-4 pt-4 space-y-6">
          <button
            onClick={() => setEtapa('cardapio')}
            className="flex items-center gap-2 text-slate-400 font-bold hover:text-white"
          >
            <ArrowLeft size={18} /> Voltar ao Cardápio
          </button>

          <div className="bg-slate-800 border border-slate-700 rounded-2xl p-4 space-y-4">
            <h2 className="text-xl font-black flex items-center gap-2">📦 Dados do Pedido</h2>
            
            <div>
              <label className="block text-sm font-bold text-slate-300 mb-1">Seu Nome:</label>
              <input
                type="text"
                value={nome}
                onChange={(e) => setNome(e.target.value)}
                placeholder="Ex: Carlos Silva"
                className="w-full bg-slate-900 border border-slate-700 rounded-xl p-3 text-white focus:outline-none focus:border-red-500"
              />
            </div>

            <div>
              <label className="block text-sm font-bold text-slate-300 mb-1">Opção de Entrega:</label>
              <div className="grid grid-cols-2 gap-2">
                {['Entrega', 'Retirar no Local'].map((op) => (
                  <button
                    key={op}
                    onClick={() => setTipoEntrega(op)}
                    className={`py-2.5 rounded-xl font-bold text-sm border ${
                      tipoEntrega === op
                        ? 'bg-red-500 text-white border-red-500'
                        : 'bg-slate-900 text-slate-400 border-slate-700'
                    }`}
                  >
                    {op}
                  </button>
                ))}
              </div>
            </div>

            {tipoEntrega === 'Entrega' && (
              <>
                <div>
                  <label className="block text-sm font-bold text-slate-300 mb-1">Selecione o Bairro:</label>
                  <select
                    value={bairro}
                    onChange={(e) => setBairro(e.target.value)}
                    className="w-full bg-slate-900 border border-slate-700 rounded-xl p-3 text-white focus:outline-none focus:border-red-500"
                  >
                    {Object.keys(taxasBairros).map((b) => (
                      <option key={b} value={b}>{b} (R$ {taxasBairros[b].toFixed(2)})</option>
                    ))}
                  </select>
                </div>

                <div>
                  <label className="block text-sm font-bold text-slate-300 mb-1">Rua e Número:</label>
                  <input
                    type="text"
                    value={ruaNumero}
                    onChange={(e) => setRuaNumero(e.target.value)}
                    placeholder="Ex: Av. Brasil, 123"
                    className="w-full bg-slate-900 border border-slate-700 rounded-xl p-3 text-white focus:outline-none focus:border-red-500"
                  />
                </div>
              </>
            )}

            <div>
              <label className="block text-sm font-bold text-slate-300 mb-1">Forma de Pagamento:</label>
              <select
                value={formaPagamento}
                onChange={(e) => setFormaPagamento(e.target.value)}
                className="w-full bg-slate-900 border border-slate-700 rounded-xl p-3 text-white focus:outline-none focus:border-red-500"
              >
                <option value="Pix">Pix</option>
                <option value="Cartão">Cartão</option>
                <option value="Dinheiro">Dinheiro</option>
              </select>
            </div>

            {formaPagamento === 'Pix' && (
              <div className="p-3 bg-green-950/60 border border-green-500/30 rounded-xl">
                <p className="text-xs text-green-300 font-bold">📱 Chave PIX (Telefone):</p>
                <p className="text-lg font-black text-green-400 tracking-wider">{CHAVE_PIX_VAL}</p>
              </div>
            )}
          </div>

          {/* Resumo financeiro */}
          <div className="bg-slate-800 border border-slate-700 rounded-2xl p-4 space-y-2">
            <div className="flex justify-between text-sm text-slate-400">
              <span>Subtotal:</span>
              <span>R$ {subtotalProdutos.toFixed(2)}</span>
            </div>
            {tipoEntrega === 'Entrega' && (
              <div className="flex justify-between text-sm text-slate-400">
                <span>Taxa de Entrega:</span>
                <span>R$ {taxaEntrega.toFixed(2)}</span>
              </div>
            )}
            <div className="flex justify-between text-lg font-black text-white pt-2 border-t border-slate-700">
              <span>Total Final:</span>
              <span className="text-green-400">R$ {totalFinal.toFixed(2)}</span>
            </div>
          </div>
        </main>
      )}

      {/* Barra Inferior Flutuante (Carrinho) */}
      {totalItens > 0 && (
        <div className="fixed bottom-0 left-0 right-0 p-4 bg-slate-950/90 backdrop-blur border-t border-slate-800 z-30">
          <div className="max-w-xl mx-auto flex items-center justify-between gap-4">
            <div>
              <p className="text-xs text-slate-400">{totalItens} {totalItens === 1 ? 'item' : 'itens'}</p>
              <p className="text-xl font-black text-green-400">R$ {totalFinal.toFixed(2)}</p>
            </div>

            {etapa === 'cardapio' ? (
              <button
                onClick={() => setEtapa('checkout')}
                className="flex-1 max-w-xs py-3.5 bg-green-500 hover:bg-green-600 text-white font-black rounded-xl flex items-center justify-center gap-2 shadow-lg shadow-green-500/20 active:scale-95 transition-all"
              >
                <ShoppingBag size={18} /> Ver Pedido
              </button>
            ) : (
              <button
                onClick={enviarWhatsApp}
                className="flex-1 max-w-xs py-3.5 bg-green-500 hover:bg-green-600 text-white font-black rounded-xl flex items-center justify-center gap-2 shadow-lg shadow-green-500/20 active:scale-95 transition-all"
              >
                <Send size={18} /> Enviar Pedido
              </button>
            )}
          </div>
        </div>
      )}
    </div>
  );
}