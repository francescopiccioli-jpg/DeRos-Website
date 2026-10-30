# DeRos menu, from "Menu_De_Ros_impaginato_1.docx" and "Dolci_e_distillati_DeRos_impaginato_1.docx" (October 2026).
# Italian and English text from the documents; English desserts and all Russian are draft translations.
# Allergen codes copied as they appear in the documents (some codes exceed the 14-item legend: to verify).

def I(it, en, ru, price, dit="", den="", dru="", al="", unit=False):
    return dict(it=it, en=en, ru=ru, dit=dit, den=den, dru=dru, price=price, al=al, unit=unit)

INTRO = {
    "it": "Benvenuti in un viaggio tra i sapori del mare, dove ogni piatto racconta una storia di freschezza, tradizione e creatività.",
    "en": "Welcome to a journey through the flavours of the sea, where every dish tells a story of freshness, tradition and creativity.",
    "ru": "Добро пожаловать в путешествие по вкусам моря, где каждое блюдо рассказывает историю свежести, традиций и творчества.",
}
TAGLINE = {"it": "Freschezza · Tradizione · Creatività", "en": "Freshness · Tradition · Creativity", "ru": "Свежесть · Традиции · Творчество"}
OUR_MENU = {"it": "Il nostro menu", "en": "Our menu", "ru": "Наше меню"}

FOOD = [
 ("raw", {"it": "Cruderìa", "en": "Raw bar", "ru": "Сырые морепродукты"}, [
  I("Ostriche Gillardeau", "Gillardeau oysters", "Устрицы Gillardeau", 8, al="14", unit=True),
  I("Ostriche Gold", "Gold oysters", "Устрицы Gold", 9, al="14", unit=True),
  I("Gambero viola", "Purple shrimp", "Фиолетовая креветка", 10, al="2", unit=True),
  I("Scampo", "Langoustine", "Лангустин", 10, al="2", unit=True),
  I("Carpaccio di scampo di Sicilia", "Sicilian langoustine carpaccio", "Карпаччо из сицилийских лангустинов", 27,
    "Carpaccio di scampo di Sicilia, mostarda di clementine, finocchio arrosto e pistacchio tostato.",
    "Sicilian langoustine carpaccio, clementine mostarda, roasted fennel and toasted pistachio.",
    "Карпаччо из сицилийских лангустинов, мостарда из клементинов, запечённый фенхель и обжаренные фисташки.", "2/6/9"),
  I("Sashimi di ricciola", "Amberjack sashimi", "Сашими из лакедры", 26,
    "Sashimi di ricciola, ravanello fermentato, caprino e limone marocchino.",
    "Amberjack sashimi, fermented radish, goat cheese and Moroccan lemon.",
    "Сашими из лакедры, ферментированный редис, козий сыр и марокканский лимон.", "4/5/12/22"),
  I("Tartare di gambero viola", "Purple shrimp tartare", "Тартар из фиолетовой креветки", 28,
    "Tartare di gambero viola, mela verde, lime e gin.",
    "Purple shrimp tartare, green apple, lime and gin.",
    "Тартар из фиолетовой креветки, зелёное яблоко, лайм и джин.", "2/13"),
  I("Tartare di wagyu", "Wagyu tartare", "Тартар из вагю", 30,
    "Tartare di wagyu con cetriolino fermentato, scalogno e mandorle tostate.",
    "Wagyu tartare with fermented gherkin, shallot and toasted almonds.",
    "Тартар из вагю с ферментированным корнишоном, луком-шалотом и обжаренным миндалём.", "6/12/22"),
 ]),
 ("starters", {"it": "Antipasti", "en": "Starters", "ru": "Закуски"}, [
  I("Calamaro e radice bianca", "Squid and white roots", "Кальмар и белые корнеплоды", 24,
    "Calamaro tiepido con purea di sedano rapa e topinambur, menta, erba cipollina e limone nero.",
    "Warm squid with celeriac and Jerusalem artichoke purée, mint, chives and black lemon.",
    "Тёплый кальмар с пюре из корня сельдерея и топинамбура, мятой, шнитт-луком и чёрным лимоном.", "1/14"),
  I("Polpo e lardo", "Octopus and lardo", "Осьминог и лардо", 28,
    "Polpo alla brace in crosta di lardo con crema di porro e nocciole.",
    "Grilled octopus in a lardo crust, with leek and hazelnut cream.",
    "Осьминог на гриле в корочке из лардо с кремом из лука-порея и фундука.", "6/12/17/22"),
  I("Barbabietola rossa fermentata", "Fermented beetroot", "Ферментированная свёкла", 18,
    "Barbabietola fermentata con caprino, nocciole, riduzione di aceto balsamico e finocchio arrosto.",
    "Fermented beetroot with goat cheese, hazelnuts, balsamic reduction and roasted fennel.",
    "Ферментированная свёкла с козьим сыром, фундуком, бальзамической редукцией и запечённым фенхелем.", "5/6/13/22"),
  I("Frittura mista di pesce", "Mixed fried seafood", "Ассорти морепродуктов во фритюре", 27,
    "Fritto misto di gamberi, calamari, polpo e trigliette.",
    "Shrimp, squid, octopus and small red mullet, lightly fried.",
    "Креветки, кальмары, осьминог и мелкая барабулька во фритюре.", "1/2/4/17/19"),
  I("Acciughe del Cantabrico", "Cantabrian anchovies", "Кантабрийские анчоусы", 28,
    "Acciughe del Cantabrico con pane e burro chiarificato.",
    "Cantabrian anchovies with bread and clarified butter.",
    "Кантабрийские анчоусы с хлебом и топлёным маслом.", "1/4/5/19"),
  I("Centrofolo viola con aneto e cetriolo", "Violet rudderfish, dill and cucumber", "Центролоф с укропом и огурцом", 25,
    "Centrofolo viola in crosta di aneto con cetriolo acido, aceto al frutto della passione e limone.",
    "Violet rudderfish in a dill crust, with pickled cucumber, passion fruit vinegar and lemon.",
    "Центролоф в укропной корочке с маринованным огурцом, уксусом из маракуйи и лимоном.", "4"),
 ]),
 ("pasta", {"it": "Primi", "en": "First courses", "ru": "Первые блюда"}, [
  I("Zuppa di pesce", "Fish soup", "Рыбный суп", 32, "Zuppa di pesce misto.", "Mixed fish soup.", "Суп из разных видов рыбы.", "2/4/12/14/22"),
  I("Risotto con crema di friarielli e cozze", "Risotto with friarielli cream and mussels", "Ризотто с кремом из фриарьелли и мидиями", 30, al="1/5/14/17/22"),
  I("Paccheri all'astice", "Paccheri with lobster", "Паккери с омаром", 38, al="1/2/3/7/12"),
  I("Ravioli patate e castagne", "Potato and chestnut ravioli", "Равиоли с картофелем и каштанами", 28,
    "Ravioli di castagna ripieni di patate e rosmarino ai funghi selvatici.",
    "Chestnut ravioli filled with potato and rosemary, with wild mushrooms.",
    "Каштановые равиоли с начинкой из картофеля и розмарина, с лесными грибами.", "1/3/5/13/14/24"),
  I("Cappellacci ripieni", "Filled cappellacci", "Каппеллаччи с начинкой", 26,
    "Cappellacci ripieni di pollo alla cacciatora.",
    "Cappellacci filled with chicken cacciatora.",
    "Каппеллаччи с начинкой из курицы по-охотничьи («каччатора»).", "1/3/5/12/13/14/15/16/19/22"),
  I("Ravioli con ricotta e crema di scampi", "Ricotta ravioli with langoustine cream", "Равиоли с рикоттой в креме из лангустинов", 32,
    "Ravioli ripieni di ricotta, timo e limone in crema di scampi.",
    "Ravioli filled with ricotta, thyme and lemon in a langoustine cream.",
    "Равиоли с рикоттой, тимьяном и лимоном в креме из лангустинов.", "1/2/3/5/12/13/14/16/22"),
 ]),
 ("mains", {"it": "Secondi", "en": "Main courses", "ru": "Основные блюда"}, [
  I("Sgombro con piselli e cavolo rosso", "Mackerel with peas and red cabbage", "Скумбрия с горошком и красной капустой", 27,
    "Sgombro con cavolo rosso fermentato, menta e mela verde e crema di sedano rapa.",
    "Mackerel with fermented red cabbage, mint, green apple and celeriac cream.",
    "Скумбрия с ферментированной красной капустой, мятой, зелёным яблоком и кремом из корня сельдерея.", "4/12"),
  I("Branzino in crosta di sale", "Salt-crusted sea bass", "Сибас в соляной корочке", 34,
    "Branzino in crosta di sale e erbe con insalata di stagione.",
    "Sea bass in a salt and herb crust, with a seasonal salad.",
    "Сибас в корочке из соли и трав с сезонным салатом.", "1/3/4"),
  I("Tonno alla milanese", "Tuna Milanese", "Тунец по-милански", 30,
    "Trancio di tonno in pane panko servito con maionese al limone.",
    "Tuna steak in panko breadcrumbs, with lemon mayonnaise.",
    "Стейк тунца в панировке панко с лимонным майонезом.", "1/3/4/5/19"),
  I("Coda di rospo in crosta di aglio", "Monkfish in a garlic crust", "Морской чёрт в чесночной корочке", 32,
    "Coda di rospo con purea di zucca, bieta e mandorle tostate.",
    "Monkfish with pumpkin purée, Swiss chard and toasted almonds.",
    "Морской чёрт с тыквенным пюре, мангольдом и обжаренным миндалём.", "4/6/22"),
  I("Grigliata di pesce", "Mixed grill of fish and shellfish", "Рыба и морепродукты на гриле", 52,
    "Grigliata di pesce con polpi, calamari, gamberi, scampi, mazzancolle e pesce bianco.",
    "Octopus, squid, shrimp, langoustines, king prawns and white fish from the grill.",
    "Осьминог, кальмары, креветки, лангустины, королевские креветки и белая рыба на гриле.", "2/4/12"),
  I("Tagliata di wagyu con rucola selvatica e pomodori", "Wagyu tagliata with wild rocket and tomatoes", "Тальята из вагю с дикой рукколой и томатами", 60, al="7/12"),
 ]),
]

DRINKS = ("drinks", {"it": "Bevande", "en": "Beverages", "ru": "Напитки"}, [
  I("Acqua", "Water", "Вода", 4.5, "Naturale o frizzante", "Still or sparkling", "Негазированная или газированная"),
  I("Coca-Cola", "Coca-Cola", "Coca-Cola", 5),
  I("Coca-Cola Zero", "Coca-Cola Zero", "Coca-Cola Zero", 5),
  I("Calice di Prosecco", "Glass of Prosecco", "Бокал просекко", 5),
  I("Calice di Franciacorta", "Glass of Franciacorta", "Бокал франчакорты", 5),
  I("Calice di vino bianco", "Glass of white wine", "Бокал белого вина", 5),
  I("Calice di vino rosso", "Glass of red wine", "Бокал красного вина", 5),
])

DESSERT_TITLE = {"it": "Dolci e distillati", "en": "Desserts and spirits", "ru": "Десерты и крепкие напитки"}
PAIRINGS = {"it": "Abbinamenti consigliati", "en": "Suggested pairings", "ru": "Рекомендуемые сочетания"}
DESSERTS = [
 (I("Tiramisù", "Tiramisù", "Тирамису", 10,
    "Il grande classico italiano, tra la delicatezza della crema al mascarpone e l'intensità del caffè e del cacao.",
    "The great Italian classic: delicate mascarpone cream and the intensity of coffee and cocoa.",
    "Великая итальянская классика: нежный крем из маскарпоне и насыщенный вкус кофе и какао."), [
  I("Ben Ryé – Donnafugata", "Ben Ryé – Donnafugata", "Ben Ryé – Donnafugata", 14,
    "Un passito avvolgente, dalle note di frutta matura e miele, che esalta la cremosità del dessert.",
    "A rich passito with notes of ripe fruit and honey that lifts the creaminess of the dessert.",
    "Насыщенное вино пассито с нотами спелых фруктов и мёда, подчёркивающее кремовость десерта."),
  I("Diplomático Selección de Familia", "Diplomático Selección de Familia", "Diplomático Selección de Familia", 15,
    "Un rum elegante e speziato, le cui note di vaniglia e caramello incontrano l'intensità del caffè.",
    "An elegant, spiced rum whose vanilla and caramel notes meet the intensity of the coffee.",
    "Элегантный пряный ром, чьи ноты ванили и карамели встречаются с насыщенностью кофе."),
 ]),
 (I("Semifreddo al torroncino con salsa al cioccolato e rum", "Nougat semifreddo with chocolate and rum sauce", "Семифреддо с нугой и шоколадно-ромовым соусом", 10,
    "Questo dessert presenta tre componenti aromatiche principali: la frutta secca e le note tostate del torroncino, l'intensità del cioccolato e il carattere caldo del rum presente nella salsa.",
    "Three main aromatic notes: the nuts and toasted flavours of the nougat, the intensity of chocolate and the warmth of the rum in the sauce.",
    "Три главных аромата: орехи и обжаренные ноты нуги, насыщенный шоколад и тёплый характер рома в соусе."), [
  I("Zacapa XO", "Zacapa XO", "Zacapa XO", 20,
    "Un rum avvolgente, dalle note di cacao e caramello, che esalta la ricchezza del cioccolato e le sfumature tostate del torroncino.",
    "A rich rum with notes of cocoa and caramel that brings out the chocolate and the toasted hints of the nougat.",
    "Насыщенный ром с нотами какао и карамели, раскрывающий шоколад и обжаренные оттенки нуги."),
  I("Macallan 12", "Macallan 12", "Macallan 12", 20,
    "Un whisky elegante, dalle sfumature di vaniglia e spezie dolci, che accompagna la frutta secca e bilancia la cremosità del semifreddo.",
    "An elegant whisky with hints of vanilla and sweet spice that matches the nuts and balances the creaminess of the semifreddo.",
    "Элегантный виски с оттенками ванили и сладких пряностей, который сочетается с орехами и уравновешивает кремовость семифреддо."),
 ]),
 (I("Il Re Maritozzo", "Il Re Maritozzo", "Il Re Maritozzo", 12,
    "", "Soft brioche bun filled with whipped cream.", "Мягкая бриошь с начинкой из взбитых сливок."), [
  I("Il Muffato", "Il Muffato", "Il Muffato", 14,
    "Un vino dolce dalle eleganti note di miele e frutta candita, che valorizza la delicatezza della panna e la sofficità del maritozzo.",
    "A sweet wine with elegant notes of honey and candied fruit that enhances the delicate cream and the softness of the bun.",
    "Десертное вино с элегантными нотами мёда и цукатов, подчёркивающее нежность сливок и мягкость булочки."),
  I("Grappa di Prosecco", "Grappa di Prosecco", "Граппа из просекко", 12,
    "Una grappa dal carattere fresco e delicatamente fruttato, che crea un piacevole contrasto con la dolcezza della panna.",
    "A fresh, delicately fruity grappa that makes a pleasant contrast with the sweetness of the cream.",
    "Свежая, деликатно фруктовая граппа, приятно контрастирующая со сладостью сливок."),
 ]),
 (I("Tarte Tatin di mele con crema alla cannella", "Apple tarte tatin with cinnamon cream", "Яблочный тарт татен с коричным кремом", 10,
    "Mele caramellate e crema alla cannella, in un incontro di dolcezza e note speziate.",
    "Caramelised apples and cinnamon cream, where sweetness meets spice.",
    "Карамелизированные яблоки и коричный крем — встреча сладости и пряных нот."), [
  I("Brugal Visionaria", "Brugal Visionaria", "Brugal Visionaria", 20,
    "Le sfumature di caramello, vaniglia e legno tostato si intrecciano con la dolcezza delle mele cotte, accompagnando le note speziate della cannella.",
    "Hints of caramel, vanilla and toasted wood weave into the sweetness of the baked apples and follow the spice of the cinnamon.",
    "Оттенки карамели, ванили и обжаренного дерева переплетаются со сладостью печёных яблок и сопровождают пряность корицы."),
  I("Glenfiddich 15", "Glenfiddich 15", "Glenfiddich 15", 25,
    "Un whisky elegante, dalle sfumature di miele e spezie, che accompagna le mele caramellate con un finale caldo e persistente.",
    "An elegant whisky with hints of honey and spice that accompanies the caramelised apples with a warm, lingering finish.",
    "Элегантный виски с оттенками мёда и пряностей, сопровождающий карамелизированные яблоки тёплым долгим послевкусием."),
 ]),
]

ALLERGEN_TITLE = {"it": "Allergeni", "en": "Allergens", "ru": "Аллергены"}
ALLERGEN_NOTE = {"it": "I numeri tra parentesi indicano gli allergeni.", "en": "Numbers in brackets indicate allergens.", "ru": "Цифры в скобках обозначают аллергены."}
ALLERGEN_LEGAL = {
 "it": "Ai sensi dell'Allegato II del Regolamento (UE) 1169/2011, relativo alle informazioni da fornire ai consumatori, riportiamo la lista dei 14 allergeni, i quali possono essere responsabili di intolleranze ed allergie nei soggetti sensibili.",
 "en": "Pursuant to Annex II of Regulation (EU) No 1169/2011 on the provision of food information to consumers, we list the 14 allergens that may cause intolerances and allergies in sensitive individuals.",
 "ru": "В соответствии с Приложением II Регламента (ЕС) № 1169/2011 о предоставлении потребителям информации о пищевых продуктах приводим список 14 аллергенов, которые могут вызывать непереносимость и аллергию у чувствительных людей.",
}
ALLERGENS = [
 ("Cereali contenenti glutine (grano, segale, orzo, avena, farro, Kamut e i loro ceppi derivati) e prodotti derivati.",
  "Cereals containing gluten (wheat, rye, barley, oats, spelt, Kamut and their hybridised strains) and products thereof.",
  "Злаки, содержащие глютен (пшеница, рожь, ячмень, овёс, полба, камут и их гибриды), и продукты из них."),
 ("Crostacei e prodotti a base di crostacei.", "Crustaceans and products thereof.", "Ракообразные и продукты из них."),
 ("Uova e prodotti a base di uova.", "Eggs and products thereof.", "Яйца и продукты из них."),
 ("Pesce e prodotti a base di pesce.", "Fish and products thereof.", "Рыба и продукты из неё."),
 ("Latte e prodotti a base di latte.", "Milk and products thereof.", "Молоко и молочные продукты."),
 ("Arachidi e prodotti a base di arachidi.", "Peanuts and products thereof.", "Арахис и продукты из него."),
 ("Soia e prodotti a base di soia.", "Soybeans and products thereof.", "Соя и продукты из неё."),
 ("Frutta a guscio (mandorle, nocciole, noci, pistacchi) e loro prodotti.", "Tree nuts (almonds, hazelnuts, walnuts, pistachios) and products thereof.", "Орехи (миндаль, фундук, грецкие орехи, фисташки) и продукты из них."),
 ("Sedano e prodotti a base di sedano.", "Celery and products thereof.", "Сельдерей и продукты из него."),
 ("Senape e prodotti a base di senape.", "Mustard and products thereof.", "Горчица и продукты из неё."),
 ("Semi di sesamo e prodotti a base di sesamo.", "Sesame seeds and products thereof.", "Кунжут и продукты из него."),
 ("Anidride solforosa e solfiti in concentrazioni superiori a 10 mg/kg o 10 mg/litro, espressi come SO₂ totale.",
  "Sulphur dioxide and sulphites at concentrations above 10 mg/kg or 10 mg/litre, expressed as total SO₂.",
  "Диоксид серы и сульфиты в концентрации выше 10 мг/кг или 10 мг/л в пересчёте на общий SO₂."),
 ("Lupini e prodotti a base di lupini.", "Lupin and products thereof.", "Люпин и продукты из него."),
 ("Molluschi e prodotti a base di molluschi.", "Molluscs and products thereof.", "Моллюски и продукты из них."),
]
ALLERGEN_ASK = {
 "it": "Al momento dell'ordinazione vi preghiamo di informare il personale di sala di eventuali intolleranze o allergie, così da prendere tutti gli accorgimenti necessari nella preparazione dei piatti.",
 "en": "When ordering, please tell our staff about any intolerances or allergies, so that every necessary precaution can be taken in preparing your dishes.",
 "ru": "При заказе, пожалуйста, сообщите персоналу о любой непереносимости или аллергии, чтобы мы приняли все необходимые меры при приготовлении блюд.",
}
THANKS = {"it": "Grazie · La direzione", "en": "Thank you · The management", "ru": "Спасибо · Администрация"}
EACH = {"it": "cad.", "en": "each", "ru": "шт."}

def price(v, lang, unit=False):
    s = (f"{v:.2f}" if v != int(v) else str(int(v)))
    if lang != "en": s = s.replace(".", ",")
    return f"€ {s}" + (f" {EACH[lang]}" if unit else "")
