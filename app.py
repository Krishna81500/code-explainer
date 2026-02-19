from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "AIzaSyA29Y164lp8KZGksWkzrUE6LCrh-_kf5Xo"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/explain', methods=['POST'])
def explain():
    data = request.json
    code = data.get('code')
    language = data.get('language')
    
    prompt = f"""Explain the following {language} code in simple terms:

```{language}
{code}
```

Provide:
1. What the code does (overview)
2. Line-by-line explanation
3. Key concepts used
4. Potential improvements"""
    
    # Try multiple API endpoints
    endpoints = [
        f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}",
        f"https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={API_KEY}"
    ]
    
    for url in endpoints:
        try:
            payload = {
                "contents": [{
                    "parts": [{"text": prompt}]
                }]
            }
            
            response = requests.post(url, json=payload, timeout=30)
            result = response.json()
            
            if response.status_code == 200 and 'candidates' in result:
                explanation = result['candidates'][0]['content']['parts'][0]['text']
                return jsonify({'success': True, 'explanation': explanation})
        except:
            continue
    
    return jsonify({'success': False, 'error': 'API not responding. Please try again.'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
