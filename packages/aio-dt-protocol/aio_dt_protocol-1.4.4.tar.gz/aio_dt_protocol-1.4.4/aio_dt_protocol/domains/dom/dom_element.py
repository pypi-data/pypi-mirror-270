import re
import asyncio
from typing import List, Dict, Optional, Union, Literal, TYPE_CHECKING
from .types import NodeCenter, NodeRect, BoxModel, StyleProp
from ...domains.runtime.types import Script, RemoteObject
from ...exceptions import (
    CouldNotFindNodeWithGivenID, RootIDNoLongerExists, NodeNotResolved, NodeNotDescribed,
    StateError
)
if TYPE_CHECKING:
    from ...connection import Connection


def to_dict_attrs(a: list) -> Union[dict, None]:
    if not a: return None
    return {a[i]: a[i+1] for i in range(0, len(a), 2)}

class Node:
    __slots__ = (
        "_connection", "nodeId", "parentId", "backendNodeId", "nodeType", "nodeName", "localName", "nodeValue",
        "childNodeCount", "children", "attributes", "documentURL", "baseURL", "publicId", "systemId", "internalSubset",
        "xmlVersion", "name", "value", "pseudoType", "frameId", "shadowRootType", "contentDocument", "shadowRoots",
        "templateContent", "pseudoElements", "importedDocument", "distributedNodes", "isSVG", "compatibilityMode",
        "remote_object", "isolated_id"
    )

    def __init__(
        self, conn, nodeId: int,
        parentId:              Optional[int] = None,
        backendNodeId:         Optional[int] = None,
        nodeType:              Optional[int] = None,
        nodeName:              Optional[str] = None,
        localName:             Optional[str] = None,
        nodeValue:             Optional[str] = None,
        childNodeCount:        Optional[int] = None,
        children:       Optional[List[dict]] = None,
        attributes:      Optional[List[str]] = None,    # Идут в списке парами ['имя атрибута', 'значение атрибута', 'имя атрибута', 'значение атрибута', ... ]
        documentURL:           Optional[str] = None,
        baseURL:               Optional[str] = None,
        publicId:              Optional[str] = None,
        systemId:              Optional[str] = None,
        internalSubset:        Optional[str] = None,
        xmlVersion:            Optional[str] = None,
        name:                  Optional[str] = None,
        value:                 Optional[str] = None,
        pseudoType:            Optional[str] = None,    # Возможные варианты: first-line, first-letter, before, after, marker, backdrop, selection, target-text, spelling-error, grammar-error, first-line-inherited, scrollbar, scrollbar-thumb, scrollbar-button, scrollbar-track, scrollbar-track-piece, scrollbar-corner, resizer, input-list-button
        frameId:               Optional[str] = None,    # доступен по дефолту в свойствах второго потомка рута  root.children[1].frameId
        shadowRootType:        Optional[str] = None,
        contentDocument:      Optional[dict] = None,
        shadowRoots:  Optional[List["Node"]] = None,    # Появляются так же у <input /> вместо 'children'
        templateContent:    Optional["Node"] = None,
        pseudoElements: Optional[List["Node"]] = None,
        importedDocument:    Optional["Node"] = None,
        distributedNodes: Optional[List[dict]] = None,  #
        isSVG:                Optional[bool] = None,    # является ли элемент SVG-элементом
        compatibilityMode: Optional[Literal["QuirksMode", "LimitedQuirksMode", "NoQuirksMode"]] = None

    ) -> None:
        self._connection: Connection = conn
        self.nodeId = nodeId
        self.backendNodeId = backendNodeId
        self.nodeType = nodeType
        self.nodeName = nodeName
        self.localName = localName
        self.nodeValue = nodeValue

        self.parentId = parentId
        self.publicId = publicId
        self.systemId = systemId
        self.internalSubset = internalSubset

        self.childNodeCount = childNodeCount
        self.children = self._addChildren(children)
        self.attributes = to_dict_attrs(attributes)
        self.frameId = frameId
        self.documentURL = documentURL
        self.baseURL = baseURL
        self.xmlVersion = xmlVersion
        self.name = name
        self.value = value
        self.pseudoType = pseudoType

        self.shadowRoots = self._addChildren(shadowRoots)
        self.shadowRootType = shadowRootType

        self.contentDocument = self._addChild(contentDocument)
        self.templateContent = self._addChild(templateContent)
        self.pseudoElements = self._addChildren(pseudoElements)
        self.importedDocument = self._addChild(importedDocument)
        self.distributedNodes = distributedNodes
        self.isSVG = isSVG
        self.compatibilityMode = compatibilityMode

        self.remote_object: Optional[RemoteObject] = None
        self.isolated_id = None                                         # идентификатор изолированного контекста

    def __str__(self) -> str:
        return f"<Node id={self.nodeId} localName={self.localName} childNodeCount={self.childNodeCount}>"

    def _addChildren(self, children_list: Optional[List[dict]] = None) -> List["Node"]:
        """
        Вызывается рекурсивно всякий раз, когда описание нового узла содержит
            список потомков, а так же, когда уже созданному узлу запрашиваются
            его потомки посредством метода getChildNodes().
        :param children_list:        Список словарей, описывающих свойства потомков.
        :return:        List[Node]
        """
        if not children_list: return []
        list_nodes = []
        for child in children_list:
            list_nodes.append(Node(self._connection, **child))
        return list_nodes

    def _addChild(self, child: Union[dict, "Node", None] = None) -> Optional["Node"]:
        if not child: return None
        return Node(self._connection, **child) if type(child) is dict else child

    async def querySelector(self, selector: str, ignore_root_id_exists: bool = False) -> Optional["Node"]:
        """
        Выполняет DOM-запрос, возвращая объект найденного узла, или None.
            Эквивалент  === element.querySelector()
        https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-querySelector
        :param selector:                    Селектор.
        :param ignore_root_id_exists:       Игнорировать исключение при отсутствии родительского элемента.
                                                Полезно при запросах на загружающихся страницах.
        :return:        <Node>
        """
        try:
            node_id = (
                await self._connection.call("DOM.querySelector", {
                    "nodeId": self.nodeId, "selector": selector
                }))["nodeId"]
        except CouldNotFindNodeWithGivenID as e:
            if match := re.search(r"nodeId\': (\d+)", str(e)):
                if match.group(1) == str(self.nodeId):
                    if ignore_root_id_exists:
                        return None
                    raise RootIDNoLongerExists
            raise
        return Node(self._connection, node_id) if node_id else None

    async def querySelectorAll(self, selector: str, ignore_root_id_exists: bool = False) -> List["Node"]:
        """
        Выполняет DOM-запрос, возвращая список объектов найденных узлов, или пустой список.
            Эквивалент  === element.querySelectorAll()
        https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-querySelectorAll
        :param selector:                    Селектор.
        :param ignore_root_id_exists:       Игнорировать исключение при отсутствии родительского элемента.
                                                Полезно при запросах на загружающихся страницах.
        :return:        [ <Node>, <Node>, ... ]
        """
        nodes = []
        try:
            for node_id in (await self._connection.call("DOM.querySelectorAll", {
                        "nodeId": self.nodeId, "selector": selector
                    }))["nodeIds"]:
                nodes.append(Node(self._connection, node_id))
        except CouldNotFindNodeWithGivenID as e:
            if match := re.search(r"nodeId\': (\d+)", str(e)):
                if match.group(1) == str(self.nodeId):
                    if ignore_root_id_exists:
                        return []
                    raise RootIDNoLongerExists
            raise
        return nodes

    async def getChildNodes(self, depth: int = -1, pierce: bool = False) -> asyncio.Event:
        """ Запрашивает событие 'DOM.setChildNodes' для собственного узла и устанавливает
        слушателя и возвращает ожидаемый объект события, который получит уведомление о том,
        что ожидаемое событие произошло и все данные уже обработаны.
        Как только 'DOM.setChildNodes' случится для текущего идентификатора узла, слушатель
        будет отменён. Список полученных потомков узла, включая текстовые будет доступен
        через его свойство 'children'.

        !ВНИМАНИЕ! Запрос потомков у <input /> не генерирует событие 'DOM.setChildNodes',
            потому как это одиночный тег, внутри которого не может быть потомков.
        :param depth:           Глубина иерархии, до которой будут получены все потомки.
                                    По умолчанию -1 == все. Чтобы задать конкретное значение,
                                    укажите любое целое число больше нуля.
        :param pierce:          Получать содержимое теневых узлов(shadowRoots, shadowDOM)?
        :return:        asyncio.Event
        """
        event = asyncio.Event()
        async def catch(data: dict) -> None:
            if data["parentId"] == self.nodeId:
                self._connection.removeListenerForEvent("DOM.setChildNodes", catch)
                self.children = self._addChildren(data["nodes"])
                event.set()

        self.children = None
        await self._connection.addListenerForEvent("DOM.setChildNodes", catch)
        await self.requestChildNodes(depth, pierce)
        return event


    async def ScrollIntoView(self, rect: dict = None) -> None:
        """
        (EXPERIMENTAL)
        Прокручивает указанный прямоугольник, в котором находится узел, если он еще не виден. После применения
            идентификатор узла становится недействителен и его придётся запрашивать вновь.
        https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-scrollIntoViewIfNeeded
        :param rect:        (optional) Прямоугольник, который будет прокручиваться в поле зрения относительно
                                поля границы узла, в пикселях CSS. Если не указан, будет использоваться
                                центр узла, аналогично Element.scrollIntoView.
                                Ожидается словарь, вида: {"x": 100, "y": 100, "width", 200, "height": 200}
        :return:        None
        """
        args = {"nodeId": self.nodeId}
        if rect:
            args.update({"rect": rect})
        await self._connection.call("DOM.scrollIntoViewIfNeeded", args)

    async def focusNode(self) -> bool:
        """
        Фокусируется на элементе.
        https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-focus
        :return:            Была ли фокусировка успешной
        """
        try:
            await self._connection.call("DOM.focus", {"nodeId": self.nodeId})
            return True
        except:
            return False

    async def getAttributes(self) -> Dict[str, str]:
        """
        Возвращает список атрибутов элемента.
        https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-getAttributes
        :return:            {'id': 'element-id', 'style': 'position:absolute;...', ...}
        """
        return to_dict_attrs(
            (await self._connection.call("DOM.getAttributes", {"nodeId": self.nodeId}))["attributes"])

    async def removeAttribute(self, name: str) -> None:
        """
        Удаляет атрибут по 'name'.
        https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-removeAttribute
        :param name:        Имя удаляемого атрибута.
        :return:
        """
        await self._connection.call("DOM.removeAttribute", {"nodeId": self.nodeId, "name": name})

    async def removeNode(self) -> None:
        """
        Удаляет себя из документа.
        https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-removeNode
        :return:
        """
        await self._connection.call("DOM.removeNode", {"nodeId": self.nodeId})

    async def getBoxModel(self) -> BoxModel:
        """
        Возвращает 'box-model' элемента.
        https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-getBoxModel
        :return:            <BoxModel>
        """
        return BoxModel(
            **(await self._connection.call("DOM.getBoxModel", {"nodeId": self.nodeId}))["model"])

    async def getOuterHTML(self) -> str:
        """
        Возвращает HTML-разметку элемента включая внешние границы тега.
        https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-getOuterHTML
        :return:            Строка HTML-разметки. '<div>Inner div text</div>'.
        """
        return (await self._connection.call("DOM.getOuterHTML", {"nodeId": self.nodeId}))["outerHTML"]

    async def getInnerHTML(self) -> str:
        """
        Возвращает HTML-разметку элемента НЕ включая внешние границы тега.
        :return:            Строка HTML-разметки. 'Inner div <div>text</div> with HTML'.
        """
        html = await self.getOuterHTML()
        if m := re.match(r"^<.*?>(.*)<.*?>$", html):
            return m.group(1)
        return html

    async def getInnerText(self) -> List[str]:
        """
        Список текстовых фрагментов составляющих общее содержимое элемента,
        расположенных между всеми его нодами.
        :return:
        """
        html = await self.getOuterHTML()
        return re.findall(r">([^<]+)<", html)

    async def setOuterHTML(self, outerHTML: str) -> None:
        """
        Устанавливает HTML-разметку для элемента. !Внимание! После этого преобразования, элемент
            получит новый идентификатор и повтороно обратиться к нему уже не получится.
        https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-setOuterHTML
        :param outerHTML:       Строка HTML-разметки. '<div>Inner div text</div>'.
        :return:
        """
        await self._connection.call("DOM.setOuterHTML", {"nodeId": self.nodeId, "outerHTML": outerHTML})

    async def moveTo(
            self, targetNodeId: int,
            insertBeforeNodeId: Optional[int] = None
    ) -> None:
        """
        Перемещает узел в новый контейнер, помещает его перед заданным якорем. В результате,
            внутренний идентификатор узла будет сменён.
        https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-moveTo
        :param targetNodeId:        Идентификатор элемента, куда будет помещён элемент.
        :param insertBeforeNodeId   (optional) Попытается поместить в этот элемент, но если он
                                        не будет найден, то перемещаемый элемент становится
                                        последним дочерним элементом 'targetNodeId'.
        :return:
        """
        args = {"nodeId": self.nodeId, "targetNodeId": targetNodeId}
        if insertBeforeNodeId:
            args.update({"insertBeforeNodeId": insertBeforeNodeId})
        self.nodeId = (await self._connection.call("DOM.moveTo", args))["nodeId"]

    async def copyTo(
            self, targetNodeId: int, insertBeforeNodeId: Optional[int] = None
    ) -> "Node":
        """
        Создает глубокую копию текущего узла и помещает ее в 'targetNodeId' перед 'insertBeforeNodeId',
            если последний указан и будет найден. Возвращает склонированный узел.
        https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-moveTo
        :param targetNodeId:        Идентификатор элемента, куда будет скопирован текущий элемент.
        :param insertBeforeNodeId   (optional) Попытается поместить в этот элемент, но если он
                                        не будет найден, то копируемый элемент становится
                                        последним дочерним элементом 'targetNodeId'.
        :return:                    <Node> - клона.
        """
        args = {"nodeId": self.nodeId, "targetNodeId": targetNodeId}
        if insertBeforeNodeId:
            args.update({"insertBeforeNodeId": insertBeforeNodeId})
        node_id = (await self._connection.call("DOM.copyTo", args))["nodeId"]
        return Node(self._connection, node_id)

    async def getContentQuads(
            self,
            backendNodeId: Optional[int] = None,
                 objectId: Optional[str] = None
    ) -> List[List[int]]:
        """
        (EXPERIMENTAL)
        Возвращает квадраты, которые описывают положение узла на странице. Этот метод может вернуть
            несколько квадратов для встроенных узлов.
        https://chromedevtools.github.io/devtools-protocol/tot/DOM/#method-getContentQuads
        :param backendNodeId:       Бэкенд идентификатор нода.
        :param objectId:            Идентификатор объекта JavaScript обертки узла.
        :return:                    quads - Массив четырехугольных вершин, где за  x всегда следует y,
                                        указывая точки по часовой стрелке.
        """
        args = {"nodeId": self.nodeId}
        if not args and backendNodeId is not None:
            args.update({"backendNodeId": backendNodeId})
        if not args and objectId is not None:
            args.update({"objectId": objectId})
        if args:
            return (await self._connection.call("DOM.getContentQuads", args))["quads"]

    async def setAttributeValue(self, attributeName: str, value: str) -> None:
        """
        Устанавливает атрибут для элемента с данным идентификатором.
            Например: await node.SetAttributeValue('class', 'class-name')
        https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-setAttributeValue
        :param attributeName:   Attribute name.
        :param value:           Attribute value.
        :return:
        """
        await self._connection.call(
            "DOM.setAttributeValue", {"nodeId": self.nodeId, "name": attributeName, "value": value})

    async def requestChildNodes(self, depth: int = 1, pierce: bool = False) -> None:
        """ Запрашивает, чтобы дочерние элементы узла с данным идентификатором возвращались
        вызывающей стороне в форме событий DOM.setChildNodes, при которых извлекаются
        не только непосредственные дочерние элементы, но и все дочерние элементы до
        указанной глубины.
        https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-requestChildNodes
        :param depth:           (optional) - Максимальная глубина, на которой должны быть получены
                                    дочерние элементы, по умолчанию равна 1. Используйте -1 для
                                    всего поддерева или укажите целое число больше 0.
        :param pierce:           (optional) - Должны ли проходить фреймы и теневые корни при
                                    возврате поддерева (по умолчанию false).
        :return:
        """
        args = {"nodeId": self.nodeId, "depth": depth, "pierce": pierce}
        await self._connection.call("DOM.requestChildNodes", args)

    async def setAttributesAsText(self, text: str, name: str = "") -> None:
        """
        Устанавливает атрибуты для элемента с заданным идентификатором. Этот метод полезен, когда пользователь
            редактирует некоторые существующие значения и типы атрибутов в нескольких парах имя/значение атрибута.
            Например(!не проверено!): await node.SetAttributesAsText("'class: class-name' 'data-id: new data-id'")
        https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-setAttributesAsText
        :param text:            Текст с рядом атрибутов. Будет анализировать этот текст с помощью HTML-парсера.
        :param name:            (optional) Имя атрибута для замены новыми атрибутами, полученными из текста,
                                    в случае успешного анализа текста.
        :return:
        """
        args = {"nodeId": self.nodeId, "text": text}
        if name:
            args.update({"name": name})
        await self._connection.call("DOM.setAttributesAsText", args)

    async def setFileInputFiles(self, files: List[str]) -> None:
        """
        Устанавливает файлы для '<input />'- элемента с заданным идентификатором.
        https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-setFileInputFiles
        :param files:           Список файлов. [ "path", "path", ... ]
        :return:
        """
        await self._connection.call("DOM.setFileInputFiles", {"nodeId": self.nodeId, "files": files})

    async def setNodeName(self, name: str) -> None:
        """
        Устанавливает новое имя узла для узла. В результате узел получит новый иденификатор.
            Например: await node.SetNewName('span')
        https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-setNodeName
        :param name:            Новое имя элемента(узла).
        :return:
        """
        self.nodeId = (await self._connection.call("DOM.setNodeName", {"nodeId": self.nodeId, "name": name}))["nodeId"]

    async def setNodeValue(self, value: str) -> None:
        """
        Устанавливает значение.
        https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-setNodeValue
        :param value:           Новое значение элемента(узла).
        :return:
        """
        await self._connection.call("DOM.setNodeValue", {"nodeId": self.nodeId, "value": value})

    async def setInspectedNode(self) -> None:
        """
        Позволяет консоли обращаться к этому узлу с через $ x (см. Более подробную
            информацию о функциях $ x в API командной строки).
        https://chromedevtools.github.io/devtools-protocol/tot/DOM#method-setInspectedNode
        :return:        None
        """
        await self._connection.call("DOM.setInspectedNode", {"nodeId": self.nodeId})

    async def collectClassNames(self) -> List[str]:
        """
        Собирает имена классов для выбранного узла и всех его потомков.
        https://chromedevtools.github.io/devtools-protocol/tot/DOM/#method-collectClassNamesFromSubtree
        :return:                Список имён классов.
        """
        return (await self._connection.call("DOM.collectClassNamesFromSubtree", {"nodeId": self.nodeId}))["classNames"]

    async def getNodesForSubtreeByStyle(
            self, computedStyles: List[dict],
            pierce: bool = False
    ) -> List["Node"]:
        """
        Находит узлы с заданным вычисленным стилем в поддереве текущего узла.
        https://chromedevtools.github.io/devtools-protocol/tot/DOM/#method-getNodesForSubtreeByStyle
        :param computedStyles:  Список вычисляемых CSS-свойств, соответствие которым будет проверяться.
                                    Например, найти все узлы, ширина которых = 50px, а высота = 15px
                                    [{'name': 'width', 'value': '50px'}, {'name': 'height', 'value': '15px'}]
        :param pierce:          (optional) - Следует ли исследовать так же фреймы и shadow-DOM.
        :return:                Список узлов.
        """
        args = {"nodeId": self.nodeId, "computedStyles": computedStyles}
        if pierce: args.update({"pierce": True})
        nodes = []
        for node_id in (await self._connection.call("DOM.getNodesForSubtreeByStyle", args))["nodeIds"]:
            nodes.append(Node(self._connection, node_id))
        return nodes

    async def getComputedStyle(self) -> List[StyleProp]:
        """
        Возвращает список <NodeProp> описывающих свойства указанного Узла.
        https://chromedevtools.github.io/devtools-protocol/tot/CSS/#method-getComputedStyleForNode
        :return:            [ <StyleProp>, ... ]
        """
        r = (await self._connection.call("CSS.getComputedStyleForNode", {"nodeId": self.nodeId}))["computedStyle"]
        return [StyleProp(**i) for i in r]

    async def getInlineStyles(self) -> Dict[str, dict]:
        """
        Возвращает стили, определенные встроенными (явно в атрибуте style и неявно, используя атрибуты DOM) для
            узла DOM, идентифицированного с помощью nodeId.
            !ВНИМАНИЕ! Требует включения уведомлений домена CSS и DOM.
        https://chromedevtools.github.io/devtools-protocol/tot/CSS/#method-getInlineStylesForNode
        :return:            { inlineStyle: {}, attributeStyle: {} }
        """
        return await self._connection.call("CSS.getInlineStylesForNode", {"nodeId": self.nodeId})

    # ==================================================================================================================

    async def getCenter(self) -> NodeCenter:
        """ Возвращает координаты центра узла """
        quad = (await self.getContentQuads())[0]
        x = (quad[2] - quad[0]) // 2 + quad[0]
        y = (quad[7] - quad[1]) // 2 + quad[1]
        return NodeCenter(x, y)

    async def getRect(self) -> NodeRect:
        """ Возвращает <NodeRect> свойств, описывающих пространственное положение узла """
        q = (await self.getContentQuads())[0]
        return NodeRect(q[0], q[1], q[2] - q[0], q[7] - q[1], q[0], q[2], q[1], q[7])

    async def click(self, delay: float = None, has_link: bool = False) -> None:
        """ Кликает в середину себя """
        if has_link:
            self._connection.Page.loading_state.clear()
        center = await self.getCenter()
        await self._connection.extend.action.mouseMoveTo(center.x, center.y)
        await self._connection.extend.action.clickTo(center.x, center.y, delay)

    async def describeNode(self, depth: Optional[int] = None, pierce: Optional[bool] = None) -> None:
        """
        Переописывает себя получая больше подробностей. Не требует включения домена. Не начинает
            отслеживать какие-либо объекты, можно использовать для автоматизации.
        https://chromedevtools.github.io/devtools-protocol/tot/DOM/#method-describeNode
        :param depth:               Максимальная глубина, на которой должны быть извлечены
                                        дочерние элементы, по умолчанию равна 1. Используйте
                                        -1 для всего поддерева или укажите целое число больше 0.
        :param pierce:              Должны ли проходиться iframes и теневые корни при возврате
                                        поддерева (по умолчанию false).
        :return:            <Node>
        """
        args = dict(nodeId=self.nodeId)
        if depth is not None: args.update(depth=depth)
        if pierce is not None: args.update(pierce=pierce)
        result = await self._connection.call("DOM.describeNode", args)
        # print("DOM.describeNode", result)

        for k, v in result["node"].items():
            if k in ["children", "shadowRoots", "pseudoElements"]:
                setattr(self, k, self._addChildren(v))
            elif k in ["contentDocument", "templateContent", "importedDocument"]:
                setattr(self, k, self._addChild(v))
            else:
                setattr(self, k, v)

    async def resolve(self) -> None:
        """ Получает ссылку на объект JavaScript для ноды. """
        if self.backendNodeId is None:
            raise NodeNotDescribed
        args = dict(backendNodeId=self.contentDocument.backendNodeId)
        result: dict = await self._connection.call("DOM.resolveNode", args)
        # print("DOM.resolveNode", result)
        self.remote_object = RemoteObject(**result.get("object"))

    async def request(self) -> "Node":
        """ Запрашивает ноду по ссылке на её оригинальный JavaScript объект. """
        if self.remote_object is None:
            raise NodeNotResolved
        args = dict(objectId=self.remote_object.objectId)
        result: dict = await self._connection.call("DOM.requestNode", args)
        # print(result)
        return Node(
            self._connection, result.get("nodeId"),
            frameId=self.frameId,
            nodeName=self.nodeName,
            localName=self.localName,
            attributes=self.attributes,
            contentDocument=self.contentDocument
        )

    async def requestMirror(self) -> "Node":
        """
        Создаёт JavaScript-объект для этой ноды и запрашивает ноду по ссылке на этот объект.
            Таким образом можно получать ноды для изолированных DOM-элементов, вроде iframe.
            Например:
                frame_node = await page.QuerySelector("iframe")     # находим iframe
                resolved_node = await frame_node.RequestMirror()    # получаем доступ к нему
                needle_node = resolved_node.QuerySelector("#needle-selector-in-iframe")
        """
        await self.describeNode()
        await self.resolve()
        return await self.request()

    async def buildScript(self, expression: str) -> Script:
        if not self._connection.Runtime.enabled:
            raise StateError("Domain 'Runtime' — must be enabled. Like: "
                             "await conn.Runtime.enable(True)")
        if not self._connection.context_manager.is_watch:
            raise StateError("Watch for execution contexts must be enabled with domain 'Runtime'. Like: "
                             "await conn.Runtime.enable(True)")
        if not self.frameId:
            await self.describeNode()
        if not (context := self._connection.context_manager.GetDefaultContext(
                self.frameId or self._connection.conn_id)):
            raise StateError("Something went wrong, or context was not obtained on creation.")

        return Script(self._connection, expression, context)
