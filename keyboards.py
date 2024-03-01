from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


class SubscriptionKB:
	subs_kb = InlineKeyboardMarkup()

	subs_kb.add(InlineKeyboardButton('Подписаться', url='https://t.me/kafmirec'))
	subs_kb.add(InlineKeyboardButton('Подписался', callback_data='check_subscrip'))


class MenuKB:
	menu_kb = InlineKeyboardMarkup()

	menu_kb.add(InlineKeyboardButton('ВопросОтвет', callback_data='question_answer'))
	menu_kb.add(InlineKeyboardButton('Поступи в РЭУ', callback_data='go'))


class MenuGoKB:
	menu_go_kb = InlineKeyboardMarkup()

	menu_go_kb.add(InlineKeyboardButton('Программы бакалавриата', callback_data="undergraduate_programs"))
	menu_go_kb.add(InlineKeyboardButton('Программы магистратуры', url="https://www.rea.ru/ru/org/cathedries/mireckaf/Documents/%D0%9A%D0%B0%D1%84%D0%B5%D0%B4%D1%80%D0%B0%20%D0%9C%D0%AD_%D0%9C%D0%B0%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%82%D1%83%D1%80%D0%B0_41.04.05_%D0%A2%D0%94%D0%B2%D0%9C%D0%91_2023.pdf"))
	menu_go_kb.add(InlineKeyboardButton('Программы дополнительного профессионального образования', callback_data="additional_programs"))
	menu_go_kb.add(InlineKeyboardButton('⏪Назад', callback_data="back_to_menu"))


class UndergraduateProgramsKB:
	programs_kb = InlineKeyboardMarkup()

	programs_kb.add(InlineKeyboardButton('Международные экономические отношения', url="https://www.rea.ru/ru/org/cathedries/mireckaf/Documents/%D0%9A%D0%B0%D1%84%D0%B5%D0%B4%D1%80%D0%B0%20%D0%9C%D0%AD_%D0%91%D0%B0%D0%BA%D0%B0%D0%BB%D0%B0%D0%B2%D1%80%D0%B8%D0%B0%D1%82_38.03.01_%D0%9C%D0%AD%D0%9E_2023.pdf"))
	programs_kb.add(InlineKeyboardButton('Глобальное устойчивое развитие', url="https://www.rea.ru/ru/org/cathedries/mireckaf/Documents/%D0%9A%D0%B0%D1%84%D0%B5%D0%B4%D1%80%D0%B0%20%D0%9C%D0%AD_%D0%91%D0%B0%D0%BA%D0%B0%D0%BB%D0%B0%D0%B2%D1%80%D0%B8%D0%B0%D1%82_41.03.05_%D0%93%D0%A3%D0%A0_2023.pdf"))
	programs_kb.add(InlineKeyboardButton('⏪Назад', callback_data="back_to_menu_go"))


class AdditionalProgramsKB:
	programs_kb = InlineKeyboardMarkup()

	programs_kb.add(InlineKeyboardButton('Международная торговля и торговая дипломатия', url="https://do.rea.ru/perepodgotovka/mezhdunarodnaya-torgovlya-i-torgovaya-diplomatiya"))
	programs_kb.add(InlineKeyboardButton('Международные договоры: от А до Я', url="https://do.rea.ru/povyshenie-kvalifikatsii/mezhdunarodnye-dogovory-ot-a-do-ya"))
	programs_kb.add(InlineKeyboardButton('Международные торговые термины: ИНКОТЕРМС 2020', url="https://do.rea.ru/povyshenie-kvalifikatsii/mezhdunarodnye-torgovye-terminy-inkoterms-2020"))
	programs_kb.add(InlineKeyboardButton('Организация бизнеса с арабскими партнерами', url="https://do.rea.ru/povyshenie-kvalifikatsii/organizatsiya-biznesa-s-arabskimi-partnerami"))
	programs_kb.add(InlineKeyboardButton('Основы научных исследований. Как написать и опубликовать статью', url="https://do.rea.ru/povyshenie-kvalifikatsii/osnovy-nauchnykh-issledovaniy-kak-napisat-i-opublikovat-statyu"))
	programs_kb.add(InlineKeyboardButton('Основы научных исследований.Как написать и защитить диссертацию', url="https://do.rea.ru/povyshenie-kvalifikatsii/osnovy-nauchnykh-issledovaniy-kak-napisat-i-zashchitit-dissertatsiyu"))
	programs_kb.add(InlineKeyboardButton('⏪Назад', callback_data="back_to_menu_go"))
