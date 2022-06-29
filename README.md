# How this works?

Есть две обособленные части: "мозг" и "внешность" симуляции (это подобие Model-View-Controller, только без C)

# Мозг

Сейчас в файле simulation.py много классов, они отвечают за то, чтобы всё это работало

# Про классы

class Simulation - это такая общая штука, при создании она генерирует сколько-то независимых маршрутов (class Route).

У него есть метод tick(), это своего рода "15 минут прошло, покажи как картина выглядит сейчас", вообще время отсчитывается в условных тиках, можно считать, что это как 15 минут или просто сколько-то минут, такой шаг симуляции
Simulation.tick() вызывает tick() для каждого Route, которые у него есть

class Route - это вот эти палочки на экране. При создании он генерирует сколько-то точек (class Checkpoint), какие-то помечает как станции (красные точки), какие-то помечает как просто точки, в которых надо отслеживать поезд, они не отображаются в интерфейсе.
Так же при создании Route создает список поездов на каждой из конечных станций (trains_straight, trains_reversed), интервал, с которым поезда должны выходить с конечных станций.

У Route тоже есть метод tick(), он вызывает tick для каждого поезда (class Train) и смотрит, если нужно отправить поезда в путь(поезда в пути хранятся в списке trains_on_the _go) и если какие-то поезда закончили маршрут

class Checkpoint - это элементики class Route, точки, где симуляция отслеживает поезда (нам нужны эти штуки, чтобы немного удобнее отрисовывать маршруты)

*remark* я попробую сделать так, чтобы на картинке маршруты пересекались, но это не самая простая задача

class Train - это сами поезда, класс нужен, чтобы отслеживать, на какой станции (или чекпоинте, который не отображается на интерфейсе) находится поезд и к нему применяется происшествие (class Accident)

У Train тоже есть tick(), он либо двигает поезд на следующий чекпоинт, либо ожидает, чтобы происшествие было исправлено

class Accident - это происшествие, у него есть какая-то сложность. Оно с некоторой вероятностью генерируется в Simulation.tick(): выбирается случайный маршрут и случайный поезж, у которого еще нет происшествия, а поезд, в свою очередь, ожидает и стоит на месте, пока происшествие, как бы, решается

# Внешность

В файле gui.py много классов, это обертка над simulation.py

Основное там - это class GUI, class RouteWrapper и функция display_trains у RouteWrapper

class GUI отрисовывает менюшку справа и инициирует отрисовку маршрутов

class RouteWrapper генерирует и отрисовывает маршрут

метод display_trains делает следующее: он смотрит на все поезда маршрута, которые в пути (trains_on_the_go) и ставит точки нужного цвета на маршруте

у этих классов тоже есть tick(), глобально, они делают Simulation.tick, заново отрисовывает маршруты(чтобы перекрыть старые поезда) и снова рисует поезда на экране


# TODO (это для меня)

1. fix trains dsappearing before got to the first station 
2. implement twisty routes displaying 
