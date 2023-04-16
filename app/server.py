from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/catt', methods=['POST'])
def run_script():
    script_name = "/usr/local/bin/catt"  # Run Catt
    args = request.json.get('args')

    if args is None:
            return jsonify(status='error', message="Please provide the 'args' parameter list in the POST request json.")

    args.insert(0, "{}".format(script_name))

    try:
        # Pass the arguments to the shell script
        output = subprocess.check_output(args, shell=False)
        return jsonify(status='success', output=output.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        return jsonify(status='error', output=e.output.decode('utf-8'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
