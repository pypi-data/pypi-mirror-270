from typing import Optional, Type
import re


class MyBaseException(Exception): pass

class EvaluateError(MyBaseException): pass

class JavaScriptError(EvaluateError): pass

class JsReferenceError(JavaScriptError): pass

class JsTypeError(JavaScriptError): pass

class JsEvalError(JavaScriptError): pass

class JsInternalError(JavaScriptError): pass

class JsRangeError(JavaScriptError): pass

class JsSyntaxError(JavaScriptError): pass

class JsURIError(JavaScriptError): pass


class PromiseEvaluateError(MyBaseException): pass

class NodeNotResolved(MyBaseException): pass

class NodeNotDescribed(MyBaseException): pass

class StateError(MyBaseException): pass

class FlagArgumentContainError(MyBaseException): pass


class TargetCrashed(MyBaseException): pass

class PositionOutOfBounds(MyBaseException): pass

class CouldNotFindNodeWithGivenID(MyBaseException): pass

class RootIDNoLongerExists(MyBaseException): pass                       # ! для QuerySelector-методов

class CouldNotComputeContentQuads(MyBaseException): pass

class NoDialogIsShowing(MyBaseException): pass                          # ! при перехвате диалоговых окон

class NoTargetWithGivenIdFound(MyBaseException): pass

class NoScriptWithGivenId(MyBaseException): pass

class UniqueContextIdNotFound(MyBaseException): pass

class InvalidRemoteObjectId(MyBaseException): pass

class NotAllowedError(MyBaseException): pass

class AnotherLocaleOverrideIsAlreadyInEffect(MyBaseException): pass     # ! при установке той же локали

class FontFamiliesCanOnlyBeSetOnce(MyBaseException): pass               # ! при установке тех же шрифтов

class GetRequestBodyBeforeRequestReceived(MyBaseException): pass        # ! получение тела до получения ответа

class NoSessionWithGivenId(MyBaseException): pass        # !

class NoSessionForGivenTargetId(MyBaseException): pass        # !

class InvalidURLError(MyBaseException): pass        # !


PROTOCOL_EXCEPTION_STORE = {
    "Target crashed": TargetCrashed,
    "Position out of bounds": PositionOutOfBounds,
    "Could not find node with given id": CouldNotFindNodeWithGivenID,
    "Could not compute content quads": CouldNotComputeContentQuads,
    "No dialog is showing": NoDialogIsShowing,
    "No target with given id found": NoTargetWithGivenIdFound,
    "No script with given id": NoScriptWithGivenId,
    "uniqueContextId not found": UniqueContextIdNotFound,
    "Invalid remote object id": InvalidRemoteObjectId,
    "Not allowed": NotAllowedError,
    "Another locale override is already in effect": AnotherLocaleOverrideIsAlreadyInEffect,
    "Font families can only be set once": FontFamiliesCanOnlyBeSetOnce,
    "Can only get response body on requests captured after headers received": GetRequestBodyBeforeRequestReceived,
    "No session with given id": NoSessionWithGivenId,
    "No session for given target id": NoSessionForGivenTargetId,
    "Cannot navigate to invalid URL": InvalidURLError,
}


JAVASCRIPT_EXCEPTIONS = {
    "ReferenceError": JsReferenceError,
    "TypeError": JsTypeError,
    "EvalError": JsEvalError,
    "InternalError": JsInternalError,
    "RangeError": JsRangeError,
    "SyntaxError": JsSyntaxError,
    "URIError": JsURIError,
}


def get_cdtp_error(error_text: str) -> Optional[Type[MyBaseException]]:
    for title, ex in PROTOCOL_EXCEPTION_STORE.items():
        if title in error_text:
            return ex
    return None
    

def highlight_eval_error(error_text: str, expression: str) -> str:
    """ Подсвечивает место в JS-коде ставшее причиной исключения.
    """
    if "SyntaxError" in error_text:
        return "\n".join([
            "\nIn your code: "
            f"\x1b[37m{expression}\x1b[0m\n"
            f"\x1b[36mSyntaxError: \x1b[91m\x1b[4m{error_text[13:]}\x1b[0m",
        ])

    line, pos = tuple(map(int, error_text.split(":")[-2:]))
    lines = expression.split("\n")
    l = lines[line - 1]
    matched = re.match(r".*?\w+\b", l[pos - 1:])
    word = matched.group(0)

    l = "".join([l[:pos - 1], f"\x1b[91m\x1b[4m{word}\x1b[0m", l[len(word) + pos - 1:]])
    return "\n".join([
        error_text,
        "\n\x1b[36mProblem in code is here: \x1b[37m",
        *lines[:line - 1], l, *lines[line:],
    ])


def highlight_promise_error(error_text: str) -> str:
    lines = error_text.split("\n")
    e_type, e_title = lines[0].split(":")

    return "".join([
        f"\x1b[36m{e_type}: \x1b[37m",
        f"\x1b[91m\x1b[4m{e_title.strip()}\x1b[0m",
        "\n", *lines[1:]
    ])
