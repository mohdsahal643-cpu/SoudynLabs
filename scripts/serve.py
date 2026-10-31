"""Local static preview with Vercel security headers, gzip and custom 404s."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import json
import gzip
import io
import sys
from urllib.parse import urlparse

ROOT=Path(__file__).resolve().parent.parent


class Handler(SimpleHTTPRequestHandler):
    def __init__(self,*args,**kwargs): super().__init__(*args,directory=str(ROOT),**kwargs)

    def end_headers(self):
        config=ROOT/'vercel.json'
        if config.exists():
            for header in json.loads(config.read_text())['headers'][0]['headers']:
                self.send_header(header['key'],header['value'])
        self.send_header('Cache-Control','no-store')
        super().end_headers()

    def send_head(self):
        relative=urlparse(self.path).path
        if any(part.startswith('.') or part in ('content','scripts') for part in Path(relative).parts):
            self.send_error(404);return None
        path=Path(self.translate_path(self.path))
        if not path.exists():
            body=(ROOT/'404.html').read_bytes()
            self.send_response(404);self.send_header('Content-Type','text/html; charset=utf-8');self.send_header('Content-Length',str(len(body)));self.end_headers();return io.BytesIO(body)
        if path.is_dir():
            if not relative.endswith('/'): return super().send_head()
            path=path/'index.html'
            if not path.exists(): self.send_error(404);return None
        body=path.read_bytes();compressed=False
        if 'gzip' in self.headers.get('Accept-Encoding','') and path.suffix in ('.html','.css','.js','.json','.xml','.svg','.txt','.webmanifest'):
            body=gzip.compress(body);compressed=True
        self.send_response(200);self.send_header('Content-Type',self.guess_type(str(path)));self.send_header('Content-Length',str(len(body)))
        if compressed:self.send_header('Content-Encoding','gzip');self.send_header('Vary','Accept-Encoding')
        self.end_headers();return io.BytesIO(body)


if __name__=='__main__':
    port=int(sys.argv[1]) if len(sys.argv)>1 else 4174
    print(f'Local preview: http://127.0.0.1:{port}',flush=True)
    ThreadingHTTPServer(('127.0.0.1',port),Handler).serve_forever()
