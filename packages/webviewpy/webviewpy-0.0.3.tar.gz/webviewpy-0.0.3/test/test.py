import os, sys

sys.path.append(os.getcwd())
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from webviewpy import *

declare_library_path(
    r"c:\Users\11737\Documents\GitHub\webviewpy\webviewpy\platform1\win32\x64\webview"
)
if __name__ == "__main__":

    html = """
<div>
  <button id="increment">+</button>
  <button id="decrement">−</button>
  <span>Counter: <span id="counterResult">0</span></span>
</div>
<hr />
<div>
  <button id="compute">Compute</button>
  <span>Result: <span id="computeResult">(not started)</span></span>
</div>
<script type="module">
  const getElements = ids => Object.assign({}, ...ids.map(
    id => ({ [id]: document.getElementById(id) })));
  const ui = getElements([
    "increment", "decrement", "counterResult", "compute",
    "computeResult"
  ]);
  ui.increment.addEventListener("click", async () => {
    ui.counterResult.textContent = await window.count(1);
  });
  ui.decrement.addEventListener("click", async () => {
    ui.counterResult.textContent = await window.count(-1);
  });
  ui.compute.addEventListener("click", async () => {
    ui.compute.disabled = true;
    ui.computeResult.textContent = "(pending)";
    ui.computeResult.textContent = await window.compute(6, 7);
    ui.compute.disabled = false;
  });
</script>"""
    wv = Webview()
    wv.set_title("basic")
    wv.set_size(500, 500)
    count = 0

    def increment(seq, req):
        global count
        count += 10

        wv.set_size(500, 500 + count)
        return str(count)

    import threading, time, json

    def compute(seq, req):
        def _(seq, req):
            print(seq, req)
            time.sleep(1)
            _js = json.loads(req)
            wv.resolve(seq, 0, str(_js[0] + _js[1]))

        threading.Thread(
            target=_,
            args=(
                seq,
                req,
            ),
        ).start()

    wv.bind("count", (increment))
    wv.bind("compute", (compute))
    wv.set_html(html)

    def haha():
        print("?")

    wv.dispatch(haha)
    wv.run()
