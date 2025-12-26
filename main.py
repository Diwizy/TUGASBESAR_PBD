import kbb

# Jalankan server
kbb.HTTPServer(("0.0.0.0", 8000), kbb.Handler).serve_forever()
