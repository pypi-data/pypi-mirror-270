import time
import json

from .utils import img_to_str, str_to_img, Encoder


class VisoData:
    def __init__(self, src_node, src_port, feed_idx, cur_node, src_name=None):
        """

        Args:
            src_node: stream/image source module - e.g. video-feed
            src_port: output port of source module
            feed_idx: the input index at current module
            cur_node: current module
        """
        self.src_node = None
        self.src_port = None
        self.src_name = None
        self.set_src(src_node=src_node, src_port=src_port, src_name=src_name)

        self.feed_idx = feed_idx
        self.cur_node = cur_node

    def set_src(self, src_node=None, src_port=None, src_name=None):
        if src_port is None:
            src_port = {}
        if src_node is None:
            src_node = {}

        if src_name is None:
            self.src_name = self.src_node.get('name', "") if self.src_node.get('name') else self.src_node.get('type')
        else:
            self.src_name = src_name

        self.src_port = src_port
        self.src_node = src_node

    def create_viso_data(self, version=1, info=None, result=None, frame=None,
                         encoder=Encoder.JPG, with_base64=False):
        """
            Generate payload to publish
        Args:
            with_base64:
            encoder:
            version:
                0.x -> publish frame data only into redis port
                1.x or later -> publish frame + metadata into redis port
            info: additional information to add meta
            result: processing result e.g. detections
            frame: processed frame cv2.ndarray

        Returns:
            {
                "meta": {
                    "ts":
                    "module": {},
                    "source": {},
                    "frame": {}
                }
                "frame": {},
                "result": {}
            }

        """
        if version > 0:
            if encoder is None or encoder not in [Encoder.JPG, Encoder.BMP]:
                encoder = Encoder.JPG
            if with_base64 is None:
                with_base64 = True

            meta = {
                "ts": time.time(),
                "source": {
                    "source_id": self.src_node.get('id', None),
                    "type": self.src_node.get('type', None),
                    "name": self.src_node.get('name', None),
                    "source_name": self.src_name,
                    "source_key": f"{self.src_node.get('id')}_{self.src_port}",
                    "source_port_idx": self.src_port,
                },
                "module": {
                    "id": self.cur_node.get('id'),
                    "type": self.cur_node.get('type'),
                    "port_idx": self.feed_idx
                },
                "frame": {}
            }

            # if info is None:
            #     info = {}
            if info and isinstance(info, dict):
                for key, val in info.items():
                    meta['key'] = val

            if result is None:
                result = []

            if frame is not None:
                frame_as_text = img_to_str(image=frame, encoder=encoder, with_base64=with_base64)
                meta['frame'] = {
                    "encoder": encoder,
                    "with_base64": with_base64
                }
            else:
                frame_as_text = None

            payload = {
                "meta": meta,
                "result": result,
                "frame": frame_as_text
            }
            return payload
        else:  # version 0.2.15 or lower
            if frame is not None:
                return img_to_str(image=frame, encoder=Encoder.JPG, with_base64=True)
            else:
                return None

    def parse_viso_data(self, data, version=1, encoder=None, with_base64=None):
        """

        Args:
            data:
            version:
            encoder:
            with_base64:

        Returns:

        """
        if isinstance(data, bytes):
            data = json.loads(data.decode())

        if version == 0:
            return str_to_img(img_as_str=data, encoder=Encoder.JPG, with_base64=True)
        else:
            if encoder is None or encoder not in [Encoder.JPG, Encoder.BMP]:
                encoder = Encoder.JPG
            if with_base64 is None:
                with_base64 = True

            source_info = data.get('meta', {}).get("source")
            if not self.src_port or self.src_node == {}:
                self.src_node = {
                    "id": source_info.get('source_id', None),
                    "type": source_info.get('type', None),
                    "name": source_info.get('name', None)
                }
            if not self.src_port or self.src_port == {}:
                self.src_port = source_info.get("source_port_idx")

            if not self.src_name:
                self.src_name = source_info.get('source_name', "")

            # if source_info.get("source_id") != self.src_node.get('id'):
            #     source_info["source_id"] = self.src_node.get('id')
            # module_info = data.get('meta', {}).get("module")
            # if module_info.get("id") != self.cur_node.get('id'):
            #     module_info["id"] = self.cur_node.get('id')

            frame_info = data.get('meta', {}).get("frame")
            encoder = frame_info.get('encoder', encoder)
            with_base64 = frame_info.get('with_base64', with_base64)

            frame_data = data.get('frame', None)
            frame = str_to_img(img_as_str=frame_data, encoder=encoder, with_base64=with_base64)
            data['frame'] = frame
            return data
