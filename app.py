import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'student-scribble-app'
app.config["MONGO_URI"] = 'mongodb+srv://root:Ipod5009@myfirstcluster-2pohw.mongodb.net/student-scribble-app?retryWrites=true'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_notes')
def get_notes():
    return render_template("notes.html", notes=mongo.db.notes.find())
    
@app.route('/add_note')
def add_note():
    return render_template('addnotes.html',
    subjects=mongo.db.subjects.find())
    
     

@app.route('/insert_note', methods=['POST'])
def insert_note():
    notes =  mongo.db.notes
    notes.insert_one(request.form.to_dict())
    return redirect(url_for('get_notes'))
     
     
     
@app.route('/edit_task/<note_id>')
def edit_task(note_id):
    the_note =  mongo.db.notes.find_one({"_id": ObjectId(note_id)})
    all_subjects =  mongo.db.subjects.find()
    return render_template('editnote.html', note=the_note,
                        subjects=all_subjects)
                           
                          
@app.route('/update_note/<note_id>', methods=["POST"])
def update_note(note_id):
    notes = mongo.db.notes
    notes.update( {'_id': ObjectId(note_id)},
    {
        'task_name':request.form.get('task_name'),
        'subject_name':request.form.get('subject_name'),
        'subject_description': request.form.get('subject_description'),
        'due_date': request.form.get('due_date'),
        'complete':request.form.get('complete')
    })
    return redirect(url_for('get_notes'))
    
    
@app.route('/delete_task/<note_id>')
def delete_task(note_id):
    mongo.db.notes.remove({'_id': ObjectId(note_id)})
    return redirect(url_for('get_notes'))
    
    
@app.route('/get_subjects')
def get_subjects():
    return render_template('subjects.html',
    subjects=mongo.db.subjects.find())
    
@app.route('/edit_subject/<subject_id>')
def edit_subject(subject_id):
    return render_template('editsubject.html',
    subject=mongo.db.subjects.find_one({'_id': ObjectId(subject_id)}))
    
@app.route('/update_subject/<subject_id>', methods=['POST'])
def update_subject(subject_id):
    mongo.db.subjects.update(
        {'_id': ObjectId(subject_id)},
        {'subject_name': request.form.get('subject_name')})
    return redirect(url_for('get_subjects'))
    
@app.route('/delete_subject/<subject_id>')
def delete_subject(subject_id):
    mongo.db.subjects.remove({'_id': ObjectId(subject_id)})
    return redirect(url_for('get_subjects'))
    
@app.route('/insert_subject', methods=['POST'])
def insert_subject():
    subject_doc = {'subject_name': request.form.get('subject_name')}
    mongo.db.subjects.insert_one(subject_doc)
    return redirect(url_for('get_subjects'))

@app.route('/new_subject')
def new_subject():
    return render_template('addsubject.html')
                           
     
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)