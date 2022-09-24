from fastapi import FastAPI
import uvicorn

api = FastAPI

authors = { 'Маякосвкий':{'Нате':'Через час отсюда в чистый переулок\
вытечет по человеку ваш обрюзгший жир,\
а я вам открыл столько стихов шкатулок,\
я — бесценных слов мот и транжир.  ',
'Лиличка':'Дым табачный воздух выел.\
Комната —\
глава в крученыховском аде.\
Вспомни —\
за этим окном\
впервые\
руки твои, исступленный, гладил.\
Сегодня сидишь вот,\
сердце в железе.\
День еще —\
выгонишь,\
можешь быть, изругав.',
'Четырёхэтажная халтура':'В центре мира\
стоит Гиз —\
оправдывает штаты служебный раж.\
Чтоб книгу\
народ\
зубами грыз,\
наворачивается\
миллионный тираж'},

'Толстой':{'Война и мир':'начинается новое, хорошее. Пока есть жизнь, есть и счастье.',
'Анна Каренина':'Уважение выдумали для того, чтобы скрывать пустое место, где должна быть любовь.\
Я настолько горда, что никогда не позволю себе любить человека, который меня не любит.',
'Воскресенье':'Люди как реки: вода во всех одинаковая и везде одна и та же, но каждая река бывает то узкая, то быстрая, то широкая, то тихая. Так и люди. Каждый человек носит в себе зачатки всех свойств людских и иногда проявляет одни, иногда другие и бывает часто совсем непохож на себя, оставаясь одним и самим собою.',},

'Пушкин':{'Я помню чудное мгновенье':'Я помню чудное мгновенье:\
Передо мной явилась ты,\
Как мимолетное виденье,\
Как гений чистой красоты.\
В томленьях грусти безнадежной,\
В тревогах шумной суеты,\
Звучал мне долго голос нежный\
И снились милые черты.',
'Пророк':'Духовной жаждою томим,\
В пустыне мрачной я влачился, —\
И шестикрылый серафим\
На перепутье мне явился.\
Перстами легкими как сон...',
'Зимнее утро':'Мороз и солнце; день чудесный!\
Еще ты дремлешь, друг прелестный —\
Пора, красавица, проснись:\
Открой сомкнуты негой взоры\
Навстречу северной Авроры,\
Звездою севера явись...',},


'Лермонтов':{'Бородино':'— Скажи-ка, дядя, ведь не даром\
Москва, спаленная пожаром,\
Французу отдана?\
Ведь были ж схватки боевые,\
Да, говорят, еще какие!\
Недаром помнит вся Россия\
Про день Бородина!',
'Когда волнуется желтеющая ива':'Когда волнуется желтеющая нива,\
И свежий лес шумит при звуке ветерка,\
И прячется в саду малиновая слива\
Под тенью сладостной зеленого листка;\
Когда росой обрызганный душистой,\
Румяным вечером иль утра в час златой,\
Из-под куста мне ландыш серебристый\
Приветливо кивает головой;омощно растопырив едва прораставшие крылышки...',
'Утёс':'Ночевала тучка золотая\
На груди утеса-великана;\
Утром в путь она умчалась рано,\
По лазури весело играя;\
Но остался влажный след в морщине\
Старого утеса. Одиноко\
Он стоит, задумался глубоко,\
И тихонько плачет он в пустыне.',

'Чехов':{'Элегия':'Купила лошадь сапоги,\
Протянула ноги,\
Поскакали утюги\
В царские чертоги.\
Ехал груздь верхом на палке,\
Спотыкнулся и упал',
'Басня':'Шли однажды через мостик\
Жирные китайцы,\
Впереди них, задрав хвостик,\
Торопились зайцы.\
Вдруг китайцы закричали:\
«Стой! Стреляй! Ах, ах!»\
Зайцы выше хвост задрали...',
'Разочарованным':'Минутами счастья,\
Верьте, не раз\
Живет, наслаждаясь,\
Каждый из нас.Но счастья того мы\
Не сознаем —\
И нам дорога лишь\
Память о нем.'}}

@api.get('/')

def Authors():
    NameAuthors = list(authors.keys())
    return {'Авторы':NameAuthors}

@api.get('/{name}')
def func_hello(name):
    TextNames = list(authors[name].keys())
    return {'Работы':TextNames}

@api.get('/{name}/{text}')
def hello2(name,text):
    return authors[name][text]

if __name__ == '__main__':
    uvicorn.run(app)