from flask import Blueprint, request, jsonify
from .models import get_db

bp = Blueprint('routes', __name__)

@bp.route('/manual_page/set_state', methods=['POST'])
def set_manual_page_state():
    user_id = request.json.get('user_id')
    selected_duration = request.json.get('selected_duration')

    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO manual_page_state (user_id, selected_duration)
        VALUES (?, ?)
    ''', (user_id, selected_duration))
    db.commit()

    return jsonify({"message": "Manual page state saved!"})

@bp.route('/manual_page/get_state', methods=['GET'])
def get_manual_page_state():
    user_id = request.args.get('user_id')

    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
        SELECT * FROM manual_page_state WHERE user_id = ?
    ''', (user_id,))
    result = cursor.fetchone()

    if result:
        return jsonify({
            "user_id": result[0],
            "selected_duration": result[1]
        })
    else:
        return jsonify({"message": "No data found"}), 404

@bp.route('/settings_page/set_state', methods=['POST'])
def set_settings_page_state():
    user_id = request.json.get('user_id')
    valve_opening_amount = request.json.get('valve_opening_amount')
    default_open = request.json.get('default_open')

    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO settings_page_state (user_id, valve_opening_amount, default_open)
        VALUES (?, ?, ?)
    ''', (user_id, valve_opening_amount, default_open))
    db.commit()

    return jsonify({"message": "Settings page state saved!"})

@bp.route('/settings_page/get_state', methods=['GET'])
def get_settings_page_state():
    user_id = request.args.get('user_id')

    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
        SELECT * FROM settings_page_state WHERE user_id = ?
    ''', (user_id,))
    result = cursor.fetchone()

    if result:
        return jsonify({
            "user_id": result[0],
            "valve_opening_amount": result[1],
            "default_open": result[2]
        })
    else:
        return jsonify({"message": "No data found"}), 404

@bp.route('/timer_page/set_state', methods=['POST'])
def set_irrigation_timer_state():
    user_id = request.json.get('user_id')
    selected_date = request.json.get('selected_date')
    selected_time = request.json.get('selected_time')
    selected_hours = request.json.get('selected_hours')
    selected_minutes = request.json.get('selected_minutes')
    selected_duration = request.json.get('selected_duration')

    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO irrigation_timer_state (user_id, selected_date, selected_time, selected_hours, selected_minutes, selected_duration)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (user_id, selected_date, selected_time, selected_hours, selected_minutes,selected_duration))
    db.commit()

    return jsonify({"message": "Irrigation timer state saved!"})

@bp.route('/timer_page/get_state', methods=['GET'])
def get_irrigation_timer_state():
    user_id = request.args.get('user_id')

    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
        SELECT * FROM irrigation_timer_state WHERE user_id = ?
    ''', (user_id,))
    result = cursor.fetchone()

    if result:
        return jsonify({
            "user_id": result[0],
            "selected_date": result[1],
            "selected_time": result[2],
            "selected_hours": result[3],
            "selected_minutes": result[4],
            "selected_duration":result[5]
        })
    else:
        return jsonify({"message": "No data found"}), 404
