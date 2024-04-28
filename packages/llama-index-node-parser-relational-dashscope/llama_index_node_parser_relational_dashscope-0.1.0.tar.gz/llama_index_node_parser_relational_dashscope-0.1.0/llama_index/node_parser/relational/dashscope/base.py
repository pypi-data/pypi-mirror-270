from typing import Any, Callable, List, Optional, Dict
import logging
import requests
import os
import json

from llama_index.core.bridge.pydantic import Field
from llama_index.core.node_parser.relational.base_element import BaseElementNodeParser, Element
from llama_index.core.schema import BaseNode, TextNode


class DashScopeJsonNodeParser(BaseElementNodeParser):
    """DashScope Json format element node parser.

    Splits a json format document from DashScope Parse into Text Nodes and Index Nodes
    corresponding to embedded objects (e.g. tables).
    """
    service_url: str = Field(
        default="https://int-dashscope.aliyuncs.com/api/v1/indeces/component/configed_transformations/spliter",
        description="URL of the service endpoint."
    )
    try_count_limit: int = Field(
        default=10,
        description="Maximum number of retry attempts."
    )
    chunk_size: int = Field(
        default=500,
        description="Size of each chunk to process."
    )
    overlap_size: int = Field(
        default=100,
        description="Overlap size between consecutive chunks."
    )
    separator: str = Field(
        default=" |,|，|。|？|！|\n|\?|\!",
        description="Separator characters for splitting texts."
    )
    pip: bool = Field(
        default=False,
        description="Flag to enable or disable PIP."
    )
    input_type: str = Field(
        default="DASHCOPE_DOCMIND",
        description="parse format type."
    )

    @classmethod
    def class_name(cls) -> str:
        return "DashScopeJsonNodeParser"

    def get_nodes_from_node(self, node: TextNode) -> List[BaseNode]:
        """Get nodes from node."""
        ftype = node.metadata.get('parse_fmt_type', self.input_type)
        assert ftype in ['DASHCOPE_DOCMIND'], f"Unexpected parse_fmt_type: {node.metadata.get('parse_fmt_type', '')}"

        ftype_map = {
            "DASHCOPE_DOCMIND": "idp",
        }
        my_input = dict()
        my_input["text"] = node.get_content()
        my_input["file_type"] = ftype_map.get(ftype, ftype)
        my_input["chunk_size"] = self.chunk_size
        my_input["overlap_size"] = self.overlap_size
        my_input["language"] = "cn"
        my_input["separator"] = self.separator
        my_input["pip"] = self.pip
        
        try_count = 0
        response_text = self.post_service(my_input)
        while response_text is None and try_count < self.try_count_limit:
            try_count += 1
            response_text = self.post_service(my_input)
        if response_text is None:
            logging.error("DashScopeJsonNodeParser Failed to get response from service")
            return []
            
        return self.parse_result(response_text, node)

    def post_service(self, my_input):
        DASHSCOPE_API_KEY = os.environ.get("DASHSCOPE_API_KEY", None)
        if DASHSCOPE_API_KEY is None:
            logging.error("DASHSCOPE_API_KEY is not set")
            raise ValueError("DASHSCOPE_API_KEY is not set")
        headers = {
            "Content-Type": "application/json",
            "Accept-Encoding": "utf-8",
            'Authorization': 'Bearer ' + DASHSCOPE_API_KEY,
        }
        try:
            response = requests.post(self.service_url, data=json.dumps(my_input), headers=headers)
            response_text = response.json()
            if 'chunkService' in response_text:
                return response_text['chunkService']['chunkResult']
            else:
                logging.error(f"{response_text}, try again.")
                return None
        except Exception as e:
            logging.error(f"{e}, try again.")
            return None

    def parse_result(self, content_json, document):
        nodes = []
        for data in content_json:
            text = '\n'.join([data['title'], data.get('hier_title', ''), data['content']])
            nodes.append(TextNode(metadata=document.metadata, text=text, excluded_embed_metadata_keys=document.excluded_embed_metadata_keys, \
                excluded_llm_metadata_keys=document.excluded_llm_metadata_keys))
        return nodes

    def extract_elements(
        self,
        text: str,
        mode: Optional[str] = "json",
        node_id: Optional[str] = None,
        node_metadata: Optional[Dict[str, Any]] = None,
        table_filters: Optional[List[Callable]] = None,
        **kwargs: Any,
    ) -> List[Element]:
        return []
