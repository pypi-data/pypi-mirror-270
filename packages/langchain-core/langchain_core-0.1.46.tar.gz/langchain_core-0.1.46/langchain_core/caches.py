"""
.. warning::
  Beta Feature!

**Cache** provides an optional caching layer for LLMs.

Cache is useful for two reasons:

- It can save you money by reducing the number of API calls you make to the LLM
  provider if you're often requesting the same completion multiple times.
- It can speed up your application by reducing the number of API calls you make
  to the LLM provider.

Cache directly competes with Memory. See documentation for Pros and Cons.

**Class hierarchy:**

.. code-block::

    BaseCache --> <name>Cache  # Examples: InMemoryCache, RedisCache, GPTCache
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, Optional, Sequence, Tuple

from langchain_core.outputs import Generation
from langchain_core.runnables import run_in_executor

RETURN_VAL_TYPE = Sequence[Generation]


class BaseCache(ABC):
    """This interfaces provides a caching layer for LLMs and Chat models.

    The cache interface consists of the following methods:

    - lookup: Look up a value based on a prompt and llm_string.
    - update: Update the cache based on a prompt and llm_string.
    - clear: Clear the cache.

    In addition, the cache interface provides an async version of each method.

    The default implementation of the async methods is to run the synchronous
    method in an executor. It's recommended to override the async methods
    and provide an async implementations to avoid unnecessary overhead.
    """

    @abstractmethod
    def lookup(self, prompt: str, llm_string: str) -> Optional[RETURN_VAL_TYPE]:
        """Look up based on prompt and llm_string.

        A cache implementation is expected to generate a key from the 2-tuple
        of prompt and llm_string (e.g., by concatenating them with a delimiter).

        Args:
            prompt: a string representation of the prompt.
                    In the case of a Chat model, the prompt is a non-trivial
                    serialization of the prompt into the language model.
            llm_string: A string representation of the LLM configuration.
                This is used to capture the invocation parameters of the LLM
                (e.g., model name, temperature, stop tokens, max tokens, etc.).
                These invocation parameters are serialized into a string
                representation.

        Returns:
            On a cache miss, return None. On a cache hit, return the cached value.
            The cached value is a list of Generations (or subclasses).
        """

    @abstractmethod
    def update(self, prompt: str, llm_string: str, return_val: RETURN_VAL_TYPE) -> None:
        """Update cache based on prompt and llm_string.

        The prompt and llm_string are used to generate a key for the cache.
        The key should match that of the look up method.

        Args:
            prompt: a string representation of the prompt.
                    In the case of a Chat model, the prompt is a non-trivial
                    serialization of the prompt into the language model.
            llm_string: A string representation of the LLM configuration.
                This is used to capture the invocation parameters of the LLM
                (e.g., model name, temperature, stop tokens, max tokens, etc.).
                These invocation parameters are serialized into a string
                representation.
            return_val: The value to be cached. The value is a list of Generations
                (or subclasses).
        """

    @abstractmethod
    def clear(self, **kwargs: Any) -> None:
        """Clear cache that can take additional keyword arguments."""

    async def alookup(self, prompt: str, llm_string: str) -> Optional[RETURN_VAL_TYPE]:
        """Async version of lookup."""
        return await run_in_executor(None, self.lookup, prompt, llm_string)

    async def aupdate(
        self, prompt: str, llm_string: str, return_val: RETURN_VAL_TYPE
    ) -> None:
        """Async version of aupdate."""
        return await run_in_executor(None, self.update, prompt, llm_string, return_val)

    async def aclear(self, **kwargs: Any) -> None:
        """Clear cache that can take additional keyword arguments."""
        return await run_in_executor(None, self.clear, **kwargs)


class InMemoryCache(BaseCache):
    """Cache that stores things in memory."""

    def __init__(self) -> None:
        """Initialize with empty cache."""
        self._cache: Dict[Tuple[str, str], RETURN_VAL_TYPE] = {}

    def lookup(self, prompt: str, llm_string: str) -> Optional[RETURN_VAL_TYPE]:
        """Look up based on prompt and llm_string."""
        return self._cache.get((prompt, llm_string), None)

    def update(self, prompt: str, llm_string: str, return_val: RETURN_VAL_TYPE) -> None:
        """Update cache based on prompt and llm_string."""
        self._cache[(prompt, llm_string)] = return_val

    def clear(self, **kwargs: Any) -> None:
        """Clear cache."""
        self._cache = {}

    async def alookup(self, prompt: str, llm_string: str) -> Optional[RETURN_VAL_TYPE]:
        """Look up based on prompt and llm_string."""
        return self.lookup(prompt, llm_string)

    async def aupdate(
        self, prompt: str, llm_string: str, return_val: RETURN_VAL_TYPE
    ) -> None:
        """Update cache based on prompt and llm_string."""
        self.update(prompt, llm_string, return_val)

    async def aclear(self, **kwargs: Any) -> None:
        """Clear cache."""
        self.clear()
