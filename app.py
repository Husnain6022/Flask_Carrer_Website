from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Lahore',
    'salary': 'Rs. 120k'
  },
  {
    'id': 2,
    'title': 'Data Engenier',
    'location': 'Karachi',
    'salary': 'Rs. 220k'
  },
  {
    'id': 3,
    'title': 'Frontend Developer',
    'location': 'Islamabad',
  
  },
  {
    'id': 4,
    'title': 'Backend Engenier',
    'location': 'Lahore',
    'salary': 'Rs. 420k'
  }
]


@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS)


@app.route('/api/jobs')
def lis_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
