from typing import Optional, TYPE_CHECKING
from ...data import DomainEvent
if TYPE_CHECKING:
    from ...connection import Connection


class Emulation:
    """
    #   https://chromedevtools.github.io/devtools-protocol/tot/Emulation
    """
    __slots__ = ("_connection",)

    def __init__(self, conn) -> None:
        self._connection: Connection = conn

    async def canEmulate(self) -> bool:
        """
        Сообщает, поддерживается ли эмуляция.
        https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-canEmulate
        :return:                result -> True если эмуляция поддерживается
        """
        return (await self._connection.call("Emulation.canEmulate"))["result"]

    async def clearDeviceMetricsOverride(self) -> None:
        """
        Очищает переопределённые метрики устройства.
        https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-clearDeviceMetricsOverride
        :return:
        """
        await self._connection.call("Emulation.clearDeviceMetricsOverride")

    async def clearGeolocationOverride(self) -> None:
        """
        Очищает переопределённые позицию геолокации и ошибку.
        https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-clearGeolocationOverride
        :return:
        """
        await self._connection.call("Emulation.clearGeolocationOverride")

    async def resetPageScaleFactor(self) -> None:
        """
        Запрашивает сброс масштабирования страницы до начальных значений.
        https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-resetPageScaleFactor
        :return:
        """
        await self._connection.call("Emulation.resetPageScaleFactor")

    async def setFocusEmulationEnabled(self, enabled: bool) -> None:
        """
        Включает или отключает симуляцию фокуса(когда страница активна).
        https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-setFocusEmulationEnabled
        :param enabled:         Включает, или отключает эмуляцию фокуса.
        :return:
        """
        await self._connection.call("Emulation.setFocusEmulationEnabled", {"enabled": enabled})

    async def setCPUThrottlingRate(self, rate: float) -> None:
        """
        Включает CPU "throttling", эмулируя медленный процессор.
        https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-setCPUThrottlingRate
        :param rate:            Коэффициент замедления(1 - без замедления; 2 - 2х кратное, и т.д.).
        :return:
        """
        await self._connection.call("Emulation.setCPUThrottlingRate", {"rate": rate})

    async def setDefaultBackgroundColorOverride(self, color: dict) -> None:
        """
        Устанавливает или очищает переопределение цвета фона фрейма по умолчанию. Это переопределение
            используется, если в содержимом оно не указано.
        https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-setDefaultBackgroundColorOverride
        :param color:            (optional) RGBA цвета фона по умолчанию. Если не указано, любое
                                    существующее переопределение будет очищено. Словарь вида:
                                        {
                                            "r": int[0-255],
                                            "g": int[0-255],
                                            "b": int[0-255],
                                            "a": float[0-1] -> опционально. По умолчанию: 1.
                                        }
        :return:
        """
        await self._connection.call("Emulation.setDefaultBackgroundColorOverride", {"color": color})

    async def setDeviceMetricsOverride(
            self, width: int, height: int,
            deviceScaleFactor: float = 0,
                        mobile: bool = False,
                        scale: Optional[float] = None,
                    screenWidth: Optional[int] = None,
                   screenHeight: Optional[int] = None,
                      positionX: Optional[int] = None,
                      positionY: Optional[int] = None,
            dontSetVisibleSize: Optional[bool] = None,
             screenOrientation: Optional[dict] = None,
                      viewport: Optional[dict] = None,
                displayFeature: Optional[dict] = None,
    ) -> None:
        """
        Переопределяет значения размеров экрана устройства (window.screen.width, window.screen.height,
            window.innerWidth, window.innerHeight и результаты медиа-запросов CSS, связанные с
            "device-width"/"device-height").
        https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-setDeviceMetricsOverride
        :param width:               Переопределяет значение ширины viewport в пикселях(от 0 до 10_000_000).
                                        window.innerWidth
                                        0 — выключает переопределение.
        :param height:              Переопределяет значение высоты viewport в пикселях(от 0 до 10_000_000).
                                        window.innerHeight
                                        0 — выключает переопределение.
        :param deviceScaleFactor:   Переопределяет значение масштабирования устройства. Отношение размера
                                        одного физического пикселя к размеру одного логического (CSS) пикселя.
                                        window.devicePixelRatio
                                        0 — выключает переопределение.
        :param mobile:              Эмуляция мобильного устройства. Это включает метатег области
                                        просмотра, полосы прокрутки наложения, авторазмер текста
                                        и многое другое.
        :param scale:               (optional, EXPERIMENTAL) Масштаб, применяемый к полученному изображению
                                        представления.
        :param screenWidth:         (optional, EXPERIMENTAL) Переопределяет значения ширины экрана в пикселях
                                        (от 0 до 10_000_000).
        :param screenHeight:        (optional, EXPERIMENTAL) Переопределяет значения высоты экрана в пикселях
                                        (от 0 до 10_000_000).
        :param positionX:           (optional, EXPERIMENTAL) Переопределяет X-позицию области просмотра на
                                        экране, в пикселях (от 0 до 10_000_000).
        :param positionY:           (optional, EXPERIMENTAL) Переопределяет Y-позицию области просмотра на
                                        экране, в пикселях (от 0 до 10_000_000).
        :param dontSetVisibleSize:  (optional, EXPERIMENTAL) Не устанавливайте видимый размер представления,
                                        полагайтесь на явный вызов setVisibleSize(смотри другие методы).
        :param screenOrientation:   (optional, EXPERIMENTAL) Переопределяет ориентацию экрана. Допустимые значения:
                                        {
                                            "type": str,    -> тип ориентации: portraitPrimary,
                                                                portraitSecondary, landscapePrimary,
                                                                landscapeSecondary
                                            "angle": int    -> Угол ориентации
                                        }
        :param viewport:            (optional, EXPERIMENTAL) Если установлено, видимая область страницы будет
                                        переопределена в этом окне просмотра. Это изменение окна просмотра
                                        не наблюдается на странице, например, относящиеся к области
                                        просмотра элементы не меняют позиции. Допустимые значения:
                                        {
                                            "x": float,     -> Смещение по оси X в независимых от устройства
                                                                пикселях (dip).
                                            "y": float,     -> Смещение по оси Y в независимых от устройства
                                                                пикселях (dip).
                                            "width": float, -> Ширина прямоугольника в независимых от устройства
                                                                пикселях (dip).
                                            "height": float,-> Высота прямоугольника в независимых от устройства
                                                                пикселях (dip).
                                            "scale": float  -> Коэффициент масштабирования страницы.
                                        }
        :param displayFeature:       (optional, EXPERIMENTAL) Если установлено, отображается функция многосегментного
                                        экрана. Если не установлено, поддержка нескольких сегментов отключена.
        :return:
        """
        args = {"width": width, "height": height, "deviceScaleFactor": deviceScaleFactor, "mobile": mobile}
        if scale is not None:
            args.update({"scale": scale})
        if screenWidth is not None:
            args.update({"screenWidth": screenWidth})
        if screenHeight is not None:
            args.update({"screenHeight": screenHeight})
        if positionX is not None:
            args.update({"positionX": positionX})
        if positionY is not None:
            args.update({"positionY": positionY})
        if dontSetVisibleSize is not None:
            args.update({"dontSetVisibleSize": dontSetVisibleSize})
        if screenOrientation is not None:
            args.update({"screenOrientation": screenOrientation})
        if viewport is not None:
            args.update({"viewport": viewport})
        if displayFeature is not None:
            args.update({"displayFeature": displayFeature})
        await self._connection.call("Emulation.setDeviceMetricsOverride", args)

    async def setScrollbarsHidden(self, hidden: bool) -> None:
        """
        (EXPERIMENTAL)
        https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-setScrollbarsHidden
        :param hidden:              Должны ли полосы прокрутки быть всегда скрыты.
        :return:
        """
        await self._connection.call("Emulation.setScrollbarsHidden", {"hidden": hidden})

    async def setDocumentCookieDisabled(self, disabled: bool) -> None:
        """
        (EXPERIMENTAL)
        https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-setDocumentCookieDisabled
        :param disabled:            Должен ли API document.cookie быть отключен.
        :return:
        """
        await self._connection.call("Emulation.setDocumentCookieDisabled", {"disabled": disabled})

    async def setEmitTouchEventsForMouse(self, enabled: bool, configuration: Optional[str] = None) -> None:
        """
        (EXPERIMENTAL)
        https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-setEmitTouchEventsForMouse
        :param enabled:             Должна ли быть включена эмуляция касания на основе ввода от мыши.
        :param configuration:       (optional) Конфигурация событий касания / жеста.
                                        По умолчанию: текущая платформа. Допустимые значения:
                                            mobile, desktop
        :return:
        """
        args = {"enabled": enabled}
        if configuration is not None:
            args.update({"configuration": configuration})
        await self._connection.call("Emulation.setEmitTouchEventsForMouse", args)

    async def setEmulatedMedia(self, media: str = "", features: Optional[list] = None) -> None:
        """
        Эмулирует переданный тип медиа или медиа-функцию для медиа-запросов CSS.
        https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-setEmulatedMedia
        :param media:               (optional) Тип медиа для эмуляции. Пустая строка отключает переопределение.
        :param features:            (optional) Список медиа-функций для эмуляции. Допустимые значения:
                                        [{
                                            "name": str,
                                            "value": str
                                        }, { ... }, ... ]
                                        https://chromedevtools.github.io/devtools-protocol/tot/Emulation#type-MediaFeature
        :return:
        """
        args = {"media": media}
        if features is not None:
            args.update({"features": features})
        await self._connection.call("Emulation.setEmulatedMedia", args)

    async def setEmulatedVisionDeficiency(self, type_: str = "none") -> None:
        """
        (EXPERIMENTAL)
        Эмулирует переданный дефицит зрения.
        https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-setEmulatedVisionDeficiency
        :param type_:                (optional) Недостаток зрения для эмуляции. Допустимые значения:
                                        none, achromatopsia, blurredVision, deuteranopia, protanopia, tritanopia
        :return:
        """
        await self._connection.call("Emulation.setEmulatedVisionDeficiency", {"type": type_})

    async def setGeolocationOverride(
            self,
             latitude: Optional[float] = None,
            longitude: Optional[float] = None,
             accuracy: Optional[float] = None
    ) -> None:
        """
        Переопределяет Положение или Ошибку Геолокации. Пропуск любого из параметров эмулирует
            "положение недоступно".
        https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-setGeolocationOverride
        :param latitude:            (optional) Широта.
        :param longitude:           (optional) Долгота.
        :param accuracy:            (optional) Точность.
        :return:
        """
        args = {}
        if latitude is not None:
            args.update({"latitude": latitude})
        if longitude is not None:
            args.update({"longitude": longitude})
        if accuracy is not None:
            args.update({"accuracy": accuracy})
        await self._connection.call("Emulation.setGeolocationOverride", args)

    async def setPageScaleFactor(self, pageScaleFactor: float) -> None:
        """
        (EXPERIMENTAL)
        Устанавливает переданный коэффициент масштабирования страницы.
        https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-setPageScaleFactor
        :param pageScaleFactor:     Коэффициент масштабирования страницы.
        :return:
        """
        await self._connection.call("Emulation.setPageScaleFactor", {"pageScaleFactor": pageScaleFactor})

    async def setScriptExecutionDisabled(self, value: bool) -> None:
        """
        Переключает выполнение скриптов на странице.
        https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-setScriptExecutionDisabled
        :param value:               Должно ли выполнение скриптов быть отключено на странице.
        :return:
        """
        await self._connection.call("Emulation.setScriptExecutionDisabled", {"value": value})

    async def setTouchEmulationEnabled(self, enabled: bool, maxTouchPoints: Optional[int] = None) -> None:
        """
        Включает "касания" для платформ, которые их не поддерживают.
        https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-setTouchEmulationEnabled
        :param enabled:             Должна ли эмуляция сенсорного события быть включена.
        :param maxTouchPoints:      (optional) Максимальное количество поддерживаемых точек касания.
                                        По умолчанию 1.
        :return:
        """
        args = {"enabled": enabled}
        if maxTouchPoints is not None:
            args.update({"maxTouchPoints": maxTouchPoints})
        await self._connection.call("Emulation.setTouchEmulationEnabled", args)

    async def setLocaleOverride(self, locale: Optional[str] = None) -> None:
        """
        Не работает.
        https://bugs.chromium.org/p/chromium/issues/detail?id=1073363
        Починили с версии Хромиум == 83.0.4103.97

        (EXPERIMENTAL)
        Переопределяет языковой стандарт хост-системы на указанную.
        https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-setLocaleOverride
        :param locale:              (optional) Язык C в стиле ICU (например, "en_US"). Если не указано
                                        или не задано, отключает переопределение и восстанавливает
                                        локаль системы хоста по умолчанию.
                                        https://stackoverflow.com/questions/3191664/list-of-all-locales-and-their-short-codes
        :return:
        """
        args = {}
        if locale is not None:
            args.update({"locale": locale})
        await self._connection.call("Emulation.setLocaleOverride", args)

    async def setTimezoneOverride(self, timezoneId: str = "") -> None:
        """
        (EXPERIMENTAL)
        Переопределяет часовой пояс хост-системы на указанный.
        https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-setTimezoneOverride
        :param timezoneId:          Идентификатор часового пояса("Europe/Moscow"). Если пусто,
                                        отключает переопределение и восстанавливает часовой пояс
                                        хост-системы по умолчанию.
                                        https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
        :return:
        """
        await self._connection.call("Emulation.setTimezoneOverride", {"timezoneId": timezoneId})

    async def setVisibleSize(self, width: int, height: int) -> None:
        """
        (DEPRECATED)
        (EXPERIMENTAL)
        Изменяет размер фрейма / области просмотра страницы. Обратите внимание, что это не влияет
            на контейнер фрейма (например, окно браузера). Может использоваться для создания
            скриншотов указанного размера. Не поддерживается на Android.
        https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-setVisibleSize
        :param width:               Ширина фрейма (DIP).
        :param height:              Высота фрейма (DIP).
        :return:            None
        """
        await self._connection.call("Emulation.setVisibleSize", {"width": width, "height": height})

    async def setUserAgentOverride(
            self, userAgent: str,
                acceptLanguage: Optional[str] = None,
                      platform: Optional[str] = None,
            userAgentMetadata: Optional[dict] = None
    ) -> None:
        """
        Переопределяет юзер-агент переданной строкой.
        https://chromedevtools.github.io/devtools-protocol/tot/Emulation#method-setUserAgentOverride
        :param userAgent:           Новый юзер-агент.
        :param acceptLanguage:      (optional) Язык браузера для эмуляции.
        :param platform:            (optional) Платформа браузера, которую возвращает
                                        "navigator.platform".
                                        https://www.w3schools.com/jsref/prop_nav_platform.asp
                                        https://stackoverflow.com/questions/19877924/what-is-the-list-of-possible-values-for-navigator-platform-as-of-today
        :param userAgentMetadata:   (optional, EXPERIMENTAL) Для отправки в заголовках Sec-CH-UA- * и возврата в
                                        navigator.userAgentData. Ожидатся словарь вида:
                                        {
                                            "brands": [{"brand": "brand name", "version": "brand version"}, { ... }, ... ],
                                            "fullVersion": "full version",
                                            "platform": "platform name",
                                            "platformVersion": "platform version",
                                            "architecture": "devise architecture",
                                            "model": "model",
                                            "mobile": boolean,
                                        }
        :return:            None
        """
        args = {"userAgent": userAgent}
        if acceptLanguage is not None:
            args.update({"acceptLanguage": acceptLanguage})
        if platform is not None:
            args.update({"platform": platform})
        if userAgentMetadata is not None:
            args.update({"userAgentMetadata": userAgentMetadata})
        await self._connection.call("Emulation.setUserAgentOverride", args)


class EmulationEvent(DomainEvent):
    virtualTimeBudgetExpired = "Emulation.virtualTimeBudgetExpired"
