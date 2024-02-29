from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, CallbackQuery

from config import TOKEN, ADMIN_ID, CHANNEL_ID
from keyboards import SubscriptionKB, MenuKB, MenuGoKB, UndergraduateProgramsKB, AdditionalProgramsKB

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start_cmd(message: Message):
	# Проверяем, подписан ли пользователь.
	user_id = message.from_user.id
	user_channel_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)

	if user_channel_status["status"] != 'left':
		await message.answer("Приветствуем тебя в официальном боте кафедры мировой экономики РЭУ им. Г.В.Плеханова !", reply_markup=MenuKB.menu_kb)
	else:
		await message.answer('Подпишись, иначе бот не будет работать!', reply_markup=SubscriptionKB.subs_kb)


@dp.message_handler()
async def start_cmd(message: Message):
	# Проверяем, подписан ли пользователь.
	user_id = message.from_user.id
	user_channel_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)

	if user_channel_status["status"] != 'left':
		await message.answer("Вопрос получен ✅ после проверки он будет опубликован")
		try:
			await bot.send_message(ADMIN_ID, text=message.text)
			await bot.send_message(-1002056159992, text=message.text)
		except Exception as e:
			pass


@dp.callback_query_handler(lambda c: c.data == 'check_subscrip')
async def check_subscrip(query: CallbackQuery):
	# Отправляем подтверждение обработки callback запроса
	await query.answer()
	
	user_id = query.from_user.id
	user_channel_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)

	await bot.delete_message(query.message.chat.id, query.message.message_id)
	
	if user_channel_status["status"] != 'left':
		await bot.send_message(user_id, 'Спасибо за подписку. Теперь вы можете отправлять боту вопросы! Просто напишите ваш вопрос и отправьте его.', reply_markup=MenuKB.menu_kb)
	else:
		await bot.send_message(user_id, 'Вы не подписались.', reply_markup=SubscriptionKB.subs_kb)


@dp.callback_query_handler(lambda c: c.data == 'question_answer')
async def question_answer(query: CallbackQuery):
	# Отправляем подтверждение обработки callback запроса
	await query.answer()
	
	user_id = query.from_user.id
	user_channel_status = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
	
	if user_channel_status["status"] != 'left':
		await bot.send_message(user_id, '✅ присылайте ваши вопросы для рубрики вопрос/ответ (после проверки модераторами они будут опубликованы).')
	else:
		await bot.send_message(user_id, 'Вы не подписались.', reply_markup=SubscriptionKB.subs_kb)


@dp.callback_query_handler(lambda c: c.data == 'go')
async def go(query: CallbackQuery):
	# Отправляем подтверждение обработки callback запроса
	await query.answer()
	await bot.delete_message(query.message.chat.id, query.message.message_id)
	await bot.send_message(query.from_user.id, 'Наши программы', reply_markup=MenuGoKB.menu_go_kb)


@dp.callback_query_handler(lambda c: c.data == 'undergraduate_programs')
async def undergraduate_programs(query: CallbackQuery):
	await query.answer()
	await bot.delete_message(query.message.chat.id, query.message.message_id)
	await bot.send_message(query.from_user.id, 'Программы бакалавриата', reply_markup=UndergraduateProgramsKB.programs_kb)


@dp.callback_query_handler(lambda c: c.data == 'additional_programs')
async def additional_programs(query: CallbackQuery):
	await query.answer()
	await bot.delete_message(query.message.chat.id, query.message.message_id)
	await bot.send_message(query.from_user.id, 'Программы дополнительного профессионального образования', reply_markup=AdditionalProgramsKB.programs_kb)


@dp.callback_query_handler(text='back_to_menu')
async def back_to_menu(query: CallbackQuery):
	await query.answer()
	await bot.delete_message(query.message.chat.id, query.message.message_id)
	await bot.send_message(query.from_user.id, "Приветствуем тебя в официальном боте кафедры мировой экономики РЭУ им. Г.В.Плеханова !", reply_markup=MenuKB.menu_kb)


@dp.callback_query_handler(text='back_to_menu_go')
async def back_to_menu_go(query: CallbackQuery):
	await query.answer()
	await bot.delete_message(query.message.chat.id, query.message.message_id)
	await bot.send_message(query.from_user.id, 'Наши программы', reply_markup=MenuGoKB.menu_go_kb)



if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)
