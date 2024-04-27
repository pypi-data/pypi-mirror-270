from typing import Optional, Dict, Any

from pydantic import BaseModel
from threadmem.server.models import RoleThreadModel, RoleMessageModel


class PromptModel(BaseModel):
    """An LLM prompt model"""

    id: Optional[str] = None
    thread: RoleThreadModel
    response: RoleMessageModel
    namespace: str = "default"
    metadata: Dict[str, Any] = {}
    created: Optional[float] = None
    approved: bool = False
    flagged: bool = False
