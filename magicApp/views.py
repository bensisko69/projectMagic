from django.shortcuts import render
from mtgsdk import Card, Supertype, Subtype, Type

def index(request):
	return render(request, 'app/index.html', {})

def importCard(request):
	supertypes = Supertype.all()
	for supertypes in supertypes:
		types = SuperTypes()
		types.supertype = supertypes
		types.save()
	subtypes = Subtype.all()
	for subtype in subtypes:
		sub = SubTypes()
		sub.subtype = subtype
		sub.save()
	types = Type.all()
	for type in types:
		t = Types()
		t.type = type
		t.save()
	color1 = Color()
	color1.color ="White"
	color1.colorIdentity = "W"
	color1.save()
	color2 = Color()
	color2.color = "Red"
	color2.colorIdentity = "R"
	color2.save()
	color3 = Color()
	color3.color = "Green"
	color3.colorIdentity = "G"
	color3.save()
	color4 = Color()
	color4.color = "Black"
	color4.colorIdentity = "B"
	color4.save()
	color = Color()
	color.color = "Uncolor"
	color.colorIdentity = "U"
	color.save()
	color.color = "Blue"
	color.colorIdentity = "B"
	color.save()
	i = 0
	while i <= 0:
		cards = Card.where(page=i).where(pageSize=1).all()
		if len(cards) > 0:
			for card in cards:
				c = CardU()
				c.cardName = card.name
				c.cmc = card.cmc
				c.type = card.type
				c.rarity = card.rarity
				c.text = card.text
				c.number = card.number
				"""if hasattr(card, 'manaCost'):"""
				c.mana = card.manaCost
				if card.colors:
					identity = card.colors[0]
					colors = Color.objects.filter(color=identity).values()
				c.power = card.power
				"""if hasattr(card, 'multiverseid'):"""
				c.multiverseid = card.multiverseid
				if hasattr(card, 'foreignNames'):
					for translate in card.foreignnames:
						if translate.language == "French":
							frenchTrad = CardTraduction()
							frenchTrad.imageUrl = translate.imageUrl
							frenchTrad.language = "French"
							frenchTrad.text = translate.text
							frenchTrad.cardId = translate.multiverseid
							frenchTrad.save()
							c.traduction = frenchTrad.id
				c.save()
			i += 1
		else:
			i = 1
	return render(request, 'app/index.html', {"len": len(cards)})
