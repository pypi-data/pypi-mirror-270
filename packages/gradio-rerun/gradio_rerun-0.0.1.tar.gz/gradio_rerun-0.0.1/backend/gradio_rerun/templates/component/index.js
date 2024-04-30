let be = null;
async function Bt() {
  return be || (be = (await import("./re_viewer-Ds4oCzjL.js")).WebHandle, be);
}
function Dt() {
  const n = new Uint8Array(16);
  return crypto.getRandomValues(n), Array.from(n).map((e) => e.toString(16).padStart(2, "0")).join("");
}
class Ht {
  /** @type {(import("./re_viewer.js").WebHandle) | null} */
  #e = null;
  /** @type {HTMLCanvasElement | null} */
  #l = null;
  /** @type {'ready' | 'starting' | 'stopped'} */
  #t = "stopped";
  /**
   * Start the viewer.
   *
   * @param {string | string[]} [rrd] URLs to `.rrd` files or WebSocket connections to our SDK.
   * @param {HTMLElement} [parent] The element to attach the canvas onto.
   * @returns {Promise<void>}
   */
  async start(e, t = document.body) {
    if (this.#t !== "stopped")
      return;
    this.#t = "starting", this.#l = document.createElement("canvas"), this.#l.id = Dt(), t.append(this.#l);
    let l = await Bt();
    if (this.#t === "starting" && (this.#e = new l(), await this.#e.start(this.#l.id, void 0), this.#t === "starting")) {
      if (this.#e.has_panicked())
        throw new Error(`Web viewer crashed: ${this.#e.panic_message()}`);
      e && this.open(e);
    }
  }
  /**
   * Returns `true` if the viewer is ready to connect to data sources.
   */
  get ready() {
    return this.#t === "ready";
  }
  /**
   * Open a recording.
   *
   * The viewer must have been started via `WebViewer.start`.
   *
   * @see {WebViewer.start}
   *
   * @param {string | string[]} rrd URLs to `.rrd` files or WebSocket connections to our SDK.
   */
  open(e) {
    if (!this.#e)
      throw new Error(`attempted to open \`${e}\` in a stopped viewer`);
    const t = Array.isArray(e) ? e : [e];
    for (const l of t)
      if (this.#e.add_receiver(l), this.#e.has_panicked())
        throw new Error(`Web viewer crashed: ${this.#e.panic_message()}`);
  }
  /**
   * Close a recording.
   *
   * The viewer must have been started via `WebViewer.start`.
   *
   * @see {WebViewer.start}
   *
   * @param {string | string[]} rrd URLs to `.rrd` files or WebSocket connections to our SDK.
   */
  close(e) {
    if (!this.#e)
      throw new Error(`attempted to close \`${e}\` in a stopped viewer`);
    const t = Array.isArray(e) ? e : [e];
    for (const l of t)
      if (this.#e.remove_receiver(l), this.#e.has_panicked())
        throw new Error(`Web viewer crashed: ${this.#e.panic_message()}`);
  }
  /**
   * Stop the viewer, freeing all associated memory.
   *
   * The same viewer instance may be started multiple times.
   */
  stop() {
    this.#t !== "stopped" && (this.#t = "stopped", this.#l?.remove(), this.#e?.destroy(), this.#e?.free(), this.#l = null, this.#e = null);
  }
}
const {
  SvelteComponent: Tt,
  assign: Rt,
  create_slot: Xt,
  detach: Yt,
  element: Gt,
  get_all_dirty_from_scope: Ot,
  get_slot_changes: Ut,
  get_spread_update: Jt,
  init: Kt,
  insert: Qt,
  safe_not_equal: xt,
  set_dynamic_element_data: Pe,
  set_style: V,
  toggle_class: B,
  transition_in: dt,
  transition_out: mt,
  update_slot_base: $t
} = window.__gradio__svelte__internal;
function el(n) {
  let e, t, l;
  const i = (
    /*#slots*/
    n[18].default
  ), s = Xt(
    i,
    n,
    /*$$scope*/
    n[17],
    null
  );
  let o = [
    { "data-testid": (
      /*test_id*/
      n[7]
    ) },
    { id: (
      /*elem_id*/
      n[2]
    ) },
    {
      class: t = "block " + /*elem_classes*/
      n[3].join(" ") + " svelte-nl1om8"
    }
  ], a = {};
  for (let r = 0; r < o.length; r += 1)
    a = Rt(a, o[r]);
  return {
    c() {
      e = Gt(
        /*tag*/
        n[14]
      ), s && s.c(), Pe(
        /*tag*/
        n[14]
      )(e, a), B(
        e,
        "hidden",
        /*visible*/
        n[10] === !1
      ), B(
        e,
        "padded",
        /*padding*/
        n[6]
      ), B(
        e,
        "border_focus",
        /*border_mode*/
        n[5] === "focus"
      ), B(
        e,
        "border_contrast",
        /*border_mode*/
        n[5] === "contrast"
      ), B(e, "hide-container", !/*explicit_call*/
      n[8] && !/*container*/
      n[9]), V(
        e,
        "height",
        /*get_dimension*/
        n[15](
          /*height*/
          n[0]
        )
      ), V(e, "width", typeof /*width*/
      n[1] == "number" ? `calc(min(${/*width*/
      n[1]}px, 100%))` : (
        /*get_dimension*/
        n[15](
          /*width*/
          n[1]
        )
      )), V(
        e,
        "border-style",
        /*variant*/
        n[4]
      ), V(
        e,
        "overflow",
        /*allow_overflow*/
        n[11] ? "visible" : "hidden"
      ), V(
        e,
        "flex-grow",
        /*scale*/
        n[12]
      ), V(e, "min-width", `calc(min(${/*min_width*/
      n[13]}px, 100%))`), V(e, "border-width", "var(--block-border-width)");
    },
    m(r, f) {
      Qt(r, e, f), s && s.m(e, null), l = !0;
    },
    p(r, f) {
      s && s.p && (!l || f & /*$$scope*/
      131072) && $t(
        s,
        i,
        r,
        /*$$scope*/
        r[17],
        l ? Ut(
          i,
          /*$$scope*/
          r[17],
          f,
          null
        ) : Ot(
          /*$$scope*/
          r[17]
        ),
        null
      ), Pe(
        /*tag*/
        r[14]
      )(e, a = Jt(o, [
        (!l || f & /*test_id*/
        128) && { "data-testid": (
          /*test_id*/
          r[7]
        ) },
        (!l || f & /*elem_id*/
        4) && { id: (
          /*elem_id*/
          r[2]
        ) },
        (!l || f & /*elem_classes*/
        8 && t !== (t = "block " + /*elem_classes*/
        r[3].join(" ") + " svelte-nl1om8")) && { class: t }
      ])), B(
        e,
        "hidden",
        /*visible*/
        r[10] === !1
      ), B(
        e,
        "padded",
        /*padding*/
        r[6]
      ), B(
        e,
        "border_focus",
        /*border_mode*/
        r[5] === "focus"
      ), B(
        e,
        "border_contrast",
        /*border_mode*/
        r[5] === "contrast"
      ), B(e, "hide-container", !/*explicit_call*/
      r[8] && !/*container*/
      r[9]), f & /*height*/
      1 && V(
        e,
        "height",
        /*get_dimension*/
        r[15](
          /*height*/
          r[0]
        )
      ), f & /*width*/
      2 && V(e, "width", typeof /*width*/
      r[1] == "number" ? `calc(min(${/*width*/
      r[1]}px, 100%))` : (
        /*get_dimension*/
        r[15](
          /*width*/
          r[1]
        )
      )), f & /*variant*/
      16 && V(
        e,
        "border-style",
        /*variant*/
        r[4]
      ), f & /*allow_overflow*/
      2048 && V(
        e,
        "overflow",
        /*allow_overflow*/
        r[11] ? "visible" : "hidden"
      ), f & /*scale*/
      4096 && V(
        e,
        "flex-grow",
        /*scale*/
        r[12]
      ), f & /*min_width*/
      8192 && V(e, "min-width", `calc(min(${/*min_width*/
      r[13]}px, 100%))`);
    },
    i(r) {
      l || (dt(s, r), l = !0);
    },
    o(r) {
      mt(s, r), l = !1;
    },
    d(r) {
      r && Yt(e), s && s.d(r);
    }
  };
}
function tl(n) {
  let e, t = (
    /*tag*/
    n[14] && el(n)
  );
  return {
    c() {
      t && t.c();
    },
    m(l, i) {
      t && t.m(l, i), e = !0;
    },
    p(l, [i]) {
      /*tag*/
      l[14] && t.p(l, i);
    },
    i(l) {
      e || (dt(t, l), e = !0);
    },
    o(l) {
      mt(t, l), e = !1;
    },
    d(l) {
      t && t.d(l);
    }
  };
}
function ll(n, e, t) {
  let { $$slots: l = {}, $$scope: i } = e, { height: s = void 0 } = e, { width: o = void 0 } = e, { elem_id: a = "" } = e, { elem_classes: r = [] } = e, { variant: f = "solid" } = e, { border_mode: u = "base" } = e, { padding: _ = !0 } = e, { type: k = "normal" } = e, { test_id: m = void 0 } = e, { explicit_call: p = !1 } = e, { container: C = !0 } = e, { visible: y = !0 } = e, { allow_overflow: L = !0 } = e, { scale: d = null } = e, { min_width: c = 0 } = e, q = k === "fieldset" ? "fieldset" : "div";
  const z = (h) => {
    if (h !== void 0) {
      if (typeof h == "number")
        return h + "px";
      if (typeof h == "string")
        return h;
    }
  };
  return n.$$set = (h) => {
    "height" in h && t(0, s = h.height), "width" in h && t(1, o = h.width), "elem_id" in h && t(2, a = h.elem_id), "elem_classes" in h && t(3, r = h.elem_classes), "variant" in h && t(4, f = h.variant), "border_mode" in h && t(5, u = h.border_mode), "padding" in h && t(6, _ = h.padding), "type" in h && t(16, k = h.type), "test_id" in h && t(7, m = h.test_id), "explicit_call" in h && t(8, p = h.explicit_call), "container" in h && t(9, C = h.container), "visible" in h && t(10, y = h.visible), "allow_overflow" in h && t(11, L = h.allow_overflow), "scale" in h && t(12, d = h.scale), "min_width" in h && t(13, c = h.min_width), "$$scope" in h && t(17, i = h.$$scope);
  }, [
    s,
    o,
    a,
    r,
    f,
    u,
    _,
    m,
    p,
    C,
    y,
    L,
    d,
    c,
    q,
    z,
    k,
    i,
    l
  ];
}
class nl extends Tt {
  constructor(e) {
    super(), Kt(this, e, ll, tl, xt, {
      height: 0,
      width: 1,
      elem_id: 2,
      elem_classes: 3,
      variant: 4,
      border_mode: 5,
      padding: 6,
      type: 16,
      test_id: 7,
      explicit_call: 8,
      container: 9,
      visible: 10,
      allow_overflow: 11,
      scale: 12,
      min_width: 13
    });
  }
}
const {
  SvelteComponent: il,
  append: Se,
  attr: R,
  bubble: sl,
  create_component: fl,
  destroy_component: ol,
  detach: bt,
  element: Me,
  init: rl,
  insert: ht,
  listen: al,
  mount_component: ul,
  safe_not_equal: cl,
  set_data: _l,
  set_style: ee,
  space: dl,
  text: ml,
  toggle_class: S,
  transition_in: bl,
  transition_out: hl
} = window.__gradio__svelte__internal;
function We(n) {
  let e, t;
  return {
    c() {
      e = Me("span"), t = ml(
        /*label*/
        n[1]
      ), R(e, "class", "svelte-1lrphxw");
    },
    m(l, i) {
      ht(l, e, i), Se(e, t);
    },
    p(l, i) {
      i & /*label*/
      2 && _l(
        t,
        /*label*/
        l[1]
      );
    },
    d(l) {
      l && bt(e);
    }
  };
}
function gl(n) {
  let e, t, l, i, s, o, a, r = (
    /*show_label*/
    n[2] && We(n)
  );
  return i = new /*Icon*/
  n[0]({}), {
    c() {
      e = Me("button"), r && r.c(), t = dl(), l = Me("div"), fl(i.$$.fragment), R(l, "class", "svelte-1lrphxw"), S(
        l,
        "small",
        /*size*/
        n[4] === "small"
      ), S(
        l,
        "large",
        /*size*/
        n[4] === "large"
      ), S(
        l,
        "medium",
        /*size*/
        n[4] === "medium"
      ), e.disabled = /*disabled*/
      n[7], R(
        e,
        "aria-label",
        /*label*/
        n[1]
      ), R(
        e,
        "aria-haspopup",
        /*hasPopup*/
        n[8]
      ), R(
        e,
        "title",
        /*label*/
        n[1]
      ), R(e, "class", "svelte-1lrphxw"), S(
        e,
        "pending",
        /*pending*/
        n[3]
      ), S(
        e,
        "padded",
        /*padded*/
        n[5]
      ), S(
        e,
        "highlight",
        /*highlight*/
        n[6]
      ), S(
        e,
        "transparent",
        /*transparent*/
        n[9]
      ), ee(e, "color", !/*disabled*/
      n[7] && /*_color*/
      n[12] ? (
        /*_color*/
        n[12]
      ) : "var(--block-label-text-color)"), ee(e, "--bg-color", /*disabled*/
      n[7] ? "auto" : (
        /*background*/
        n[10]
      )), ee(
        e,
        "margin-left",
        /*offset*/
        n[11] + "px"
      );
    },
    m(f, u) {
      ht(f, e, u), r && r.m(e, null), Se(e, t), Se(e, l), ul(i, l, null), s = !0, o || (a = al(
        e,
        "click",
        /*click_handler*/
        n[14]
      ), o = !0);
    },
    p(f, [u]) {
      /*show_label*/
      f[2] ? r ? r.p(f, u) : (r = We(f), r.c(), r.m(e, t)) : r && (r.d(1), r = null), (!s || u & /*size*/
      16) && S(
        l,
        "small",
        /*size*/
        f[4] === "small"
      ), (!s || u & /*size*/
      16) && S(
        l,
        "large",
        /*size*/
        f[4] === "large"
      ), (!s || u & /*size*/
      16) && S(
        l,
        "medium",
        /*size*/
        f[4] === "medium"
      ), (!s || u & /*disabled*/
      128) && (e.disabled = /*disabled*/
      f[7]), (!s || u & /*label*/
      2) && R(
        e,
        "aria-label",
        /*label*/
        f[1]
      ), (!s || u & /*hasPopup*/
      256) && R(
        e,
        "aria-haspopup",
        /*hasPopup*/
        f[8]
      ), (!s || u & /*label*/
      2) && R(
        e,
        "title",
        /*label*/
        f[1]
      ), (!s || u & /*pending*/
      8) && S(
        e,
        "pending",
        /*pending*/
        f[3]
      ), (!s || u & /*padded*/
      32) && S(
        e,
        "padded",
        /*padded*/
        f[5]
      ), (!s || u & /*highlight*/
      64) && S(
        e,
        "highlight",
        /*highlight*/
        f[6]
      ), (!s || u & /*transparent*/
      512) && S(
        e,
        "transparent",
        /*transparent*/
        f[9]
      ), u & /*disabled, _color*/
      4224 && ee(e, "color", !/*disabled*/
      f[7] && /*_color*/
      f[12] ? (
        /*_color*/
        f[12]
      ) : "var(--block-label-text-color)"), u & /*disabled, background*/
      1152 && ee(e, "--bg-color", /*disabled*/
      f[7] ? "auto" : (
        /*background*/
        f[10]
      )), u & /*offset*/
      2048 && ee(
        e,
        "margin-left",
        /*offset*/
        f[11] + "px"
      );
    },
    i(f) {
      s || (bl(i.$$.fragment, f), s = !0);
    },
    o(f) {
      hl(i.$$.fragment, f), s = !1;
    },
    d(f) {
      f && bt(e), r && r.d(), ol(i), o = !1, a();
    }
  };
}
function wl(n, e, t) {
  let l, { Icon: i } = e, { label: s = "" } = e, { show_label: o = !1 } = e, { pending: a = !1 } = e, { size: r = "small" } = e, { padded: f = !0 } = e, { highlight: u = !1 } = e, { disabled: _ = !1 } = e, { hasPopup: k = !1 } = e, { color: m = "var(--block-label-text-color)" } = e, { transparent: p = !1 } = e, { background: C = "var(--background-fill-primary)" } = e, { offset: y = 0 } = e;
  function L(d) {
    sl.call(this, n, d);
  }
  return n.$$set = (d) => {
    "Icon" in d && t(0, i = d.Icon), "label" in d && t(1, s = d.label), "show_label" in d && t(2, o = d.show_label), "pending" in d && t(3, a = d.pending), "size" in d && t(4, r = d.size), "padded" in d && t(5, f = d.padded), "highlight" in d && t(6, u = d.highlight), "disabled" in d && t(7, _ = d.disabled), "hasPopup" in d && t(8, k = d.hasPopup), "color" in d && t(13, m = d.color), "transparent" in d && t(9, p = d.transparent), "background" in d && t(10, C = d.background), "offset" in d && t(11, y = d.offset);
  }, n.$$.update = () => {
    n.$$.dirty & /*highlight, color*/
    8256 && t(12, l = u ? "var(--color-accent)" : m);
  }, [
    i,
    s,
    o,
    a,
    r,
    f,
    u,
    _,
    k,
    p,
    C,
    y,
    l,
    m,
    L
  ];
}
class kl extends il {
  constructor(e) {
    super(), rl(this, e, wl, gl, cl, {
      Icon: 0,
      label: 1,
      show_label: 2,
      pending: 3,
      size: 4,
      padded: 5,
      highlight: 6,
      disabled: 7,
      hasPopup: 8,
      color: 13,
      transparent: 9,
      background: 10,
      offset: 11
    });
  }
}
const {
  SvelteComponent: pl,
  append: Ce,
  attr: E,
  detach: yl,
  init: vl,
  insert: ql,
  noop: Fe,
  safe_not_equal: Cl,
  set_style: D,
  svg_element: he
} = window.__gradio__svelte__internal;
function Fl(n) {
  let e, t, l, i;
  return {
    c() {
      e = he("svg"), t = he("g"), l = he("path"), i = he("path"), E(l, "d", "M18,6L6.087,17.913"), D(l, "fill", "none"), D(l, "fill-rule", "nonzero"), D(l, "stroke-width", "2px"), E(t, "transform", "matrix(1.14096,-0.140958,-0.140958,1.14096,-0.0559523,0.0559523)"), E(i, "d", "M4.364,4.364L19.636,19.636"), D(i, "fill", "none"), D(i, "fill-rule", "nonzero"), D(i, "stroke-width", "2px"), E(e, "width", "100%"), E(e, "height", "100%"), E(e, "viewBox", "0 0 24 24"), E(e, "version", "1.1"), E(e, "xmlns", "http://www.w3.org/2000/svg"), E(e, "xmlns:xlink", "http://www.w3.org/1999/xlink"), E(e, "xml:space", "preserve"), E(e, "stroke", "currentColor"), D(e, "fill-rule", "evenodd"), D(e, "clip-rule", "evenodd"), D(e, "stroke-linecap", "round"), D(e, "stroke-linejoin", "round");
    },
    m(s, o) {
      ql(s, e, o), Ce(e, t), Ce(t, l), Ce(e, i);
    },
    p: Fe,
    i: Fe,
    o: Fe,
    d(s) {
      s && yl(e);
    }
  };
}
class Ll extends pl {
  constructor(e) {
    super(), vl(this, e, null, Fl, Cl, {});
  }
}
const Sl = [
  { color: "red", primary: 600, secondary: 100 },
  { color: "green", primary: 600, secondary: 100 },
  { color: "blue", primary: 600, secondary: 100 },
  { color: "yellow", primary: 500, secondary: 100 },
  { color: "purple", primary: 600, secondary: 100 },
  { color: "teal", primary: 600, secondary: 100 },
  { color: "orange", primary: 600, secondary: 100 },
  { color: "cyan", primary: 600, secondary: 100 },
  { color: "lime", primary: 500, secondary: 100 },
  { color: "pink", primary: 600, secondary: 100 }
], Be = {
  inherit: "inherit",
  current: "currentColor",
  transparent: "transparent",
  black: "#000",
  white: "#fff",
  slate: {
    50: "#f8fafc",
    100: "#f1f5f9",
    200: "#e2e8f0",
    300: "#cbd5e1",
    400: "#94a3b8",
    500: "#64748b",
    600: "#475569",
    700: "#334155",
    800: "#1e293b",
    900: "#0f172a",
    950: "#020617"
  },
  gray: {
    50: "#f9fafb",
    100: "#f3f4f6",
    200: "#e5e7eb",
    300: "#d1d5db",
    400: "#9ca3af",
    500: "#6b7280",
    600: "#4b5563",
    700: "#374151",
    800: "#1f2937",
    900: "#111827",
    950: "#030712"
  },
  zinc: {
    50: "#fafafa",
    100: "#f4f4f5",
    200: "#e4e4e7",
    300: "#d4d4d8",
    400: "#a1a1aa",
    500: "#71717a",
    600: "#52525b",
    700: "#3f3f46",
    800: "#27272a",
    900: "#18181b",
    950: "#09090b"
  },
  neutral: {
    50: "#fafafa",
    100: "#f5f5f5",
    200: "#e5e5e5",
    300: "#d4d4d4",
    400: "#a3a3a3",
    500: "#737373",
    600: "#525252",
    700: "#404040",
    800: "#262626",
    900: "#171717",
    950: "#0a0a0a"
  },
  stone: {
    50: "#fafaf9",
    100: "#f5f5f4",
    200: "#e7e5e4",
    300: "#d6d3d1",
    400: "#a8a29e",
    500: "#78716c",
    600: "#57534e",
    700: "#44403c",
    800: "#292524",
    900: "#1c1917",
    950: "#0c0a09"
  },
  red: {
    50: "#fef2f2",
    100: "#fee2e2",
    200: "#fecaca",
    300: "#fca5a5",
    400: "#f87171",
    500: "#ef4444",
    600: "#dc2626",
    700: "#b91c1c",
    800: "#991b1b",
    900: "#7f1d1d",
    950: "#450a0a"
  },
  orange: {
    50: "#fff7ed",
    100: "#ffedd5",
    200: "#fed7aa",
    300: "#fdba74",
    400: "#fb923c",
    500: "#f97316",
    600: "#ea580c",
    700: "#c2410c",
    800: "#9a3412",
    900: "#7c2d12",
    950: "#431407"
  },
  amber: {
    50: "#fffbeb",
    100: "#fef3c7",
    200: "#fde68a",
    300: "#fcd34d",
    400: "#fbbf24",
    500: "#f59e0b",
    600: "#d97706",
    700: "#b45309",
    800: "#92400e",
    900: "#78350f",
    950: "#451a03"
  },
  yellow: {
    50: "#fefce8",
    100: "#fef9c3",
    200: "#fef08a",
    300: "#fde047",
    400: "#facc15",
    500: "#eab308",
    600: "#ca8a04",
    700: "#a16207",
    800: "#854d0e",
    900: "#713f12",
    950: "#422006"
  },
  lime: {
    50: "#f7fee7",
    100: "#ecfccb",
    200: "#d9f99d",
    300: "#bef264",
    400: "#a3e635",
    500: "#84cc16",
    600: "#65a30d",
    700: "#4d7c0f",
    800: "#3f6212",
    900: "#365314",
    950: "#1a2e05"
  },
  green: {
    50: "#f0fdf4",
    100: "#dcfce7",
    200: "#bbf7d0",
    300: "#86efac",
    400: "#4ade80",
    500: "#22c55e",
    600: "#16a34a",
    700: "#15803d",
    800: "#166534",
    900: "#14532d",
    950: "#052e16"
  },
  emerald: {
    50: "#ecfdf5",
    100: "#d1fae5",
    200: "#a7f3d0",
    300: "#6ee7b7",
    400: "#34d399",
    500: "#10b981",
    600: "#059669",
    700: "#047857",
    800: "#065f46",
    900: "#064e3b",
    950: "#022c22"
  },
  teal: {
    50: "#f0fdfa",
    100: "#ccfbf1",
    200: "#99f6e4",
    300: "#5eead4",
    400: "#2dd4bf",
    500: "#14b8a6",
    600: "#0d9488",
    700: "#0f766e",
    800: "#115e59",
    900: "#134e4a",
    950: "#042f2e"
  },
  cyan: {
    50: "#ecfeff",
    100: "#cffafe",
    200: "#a5f3fc",
    300: "#67e8f9",
    400: "#22d3ee",
    500: "#06b6d4",
    600: "#0891b2",
    700: "#0e7490",
    800: "#155e75",
    900: "#164e63",
    950: "#083344"
  },
  sky: {
    50: "#f0f9ff",
    100: "#e0f2fe",
    200: "#bae6fd",
    300: "#7dd3fc",
    400: "#38bdf8",
    500: "#0ea5e9",
    600: "#0284c7",
    700: "#0369a1",
    800: "#075985",
    900: "#0c4a6e",
    950: "#082f49"
  },
  blue: {
    50: "#eff6ff",
    100: "#dbeafe",
    200: "#bfdbfe",
    300: "#93c5fd",
    400: "#60a5fa",
    500: "#3b82f6",
    600: "#2563eb",
    700: "#1d4ed8",
    800: "#1e40af",
    900: "#1e3a8a",
    950: "#172554"
  },
  indigo: {
    50: "#eef2ff",
    100: "#e0e7ff",
    200: "#c7d2fe",
    300: "#a5b4fc",
    400: "#818cf8",
    500: "#6366f1",
    600: "#4f46e5",
    700: "#4338ca",
    800: "#3730a3",
    900: "#312e81",
    950: "#1e1b4b"
  },
  violet: {
    50: "#f5f3ff",
    100: "#ede9fe",
    200: "#ddd6fe",
    300: "#c4b5fd",
    400: "#a78bfa",
    500: "#8b5cf6",
    600: "#7c3aed",
    700: "#6d28d9",
    800: "#5b21b6",
    900: "#4c1d95",
    950: "#2e1065"
  },
  purple: {
    50: "#faf5ff",
    100: "#f3e8ff",
    200: "#e9d5ff",
    300: "#d8b4fe",
    400: "#c084fc",
    500: "#a855f7",
    600: "#9333ea",
    700: "#7e22ce",
    800: "#6b21a8",
    900: "#581c87",
    950: "#3b0764"
  },
  fuchsia: {
    50: "#fdf4ff",
    100: "#fae8ff",
    200: "#f5d0fe",
    300: "#f0abfc",
    400: "#e879f9",
    500: "#d946ef",
    600: "#c026d3",
    700: "#a21caf",
    800: "#86198f",
    900: "#701a75",
    950: "#4a044e"
  },
  pink: {
    50: "#fdf2f8",
    100: "#fce7f3",
    200: "#fbcfe8",
    300: "#f9a8d4",
    400: "#f472b6",
    500: "#ec4899",
    600: "#db2777",
    700: "#be185d",
    800: "#9d174d",
    900: "#831843",
    950: "#500724"
  },
  rose: {
    50: "#fff1f2",
    100: "#ffe4e6",
    200: "#fecdd3",
    300: "#fda4af",
    400: "#fb7185",
    500: "#f43f5e",
    600: "#e11d48",
    700: "#be123c",
    800: "#9f1239",
    900: "#881337",
    950: "#4c0519"
  }
};
Sl.reduce(
  (n, { color: e, primary: t, secondary: l }) => ({
    ...n,
    [e]: {
      primary: Be[e][t],
      secondary: Be[e][l]
    }
  }),
  {}
);
function ne(n) {
  let e = ["", "k", "M", "G", "T", "P", "E", "Z"], t = 0;
  for (; n > 1e3 && t < e.length - 1; )
    n /= 1e3, t++;
  let l = e[t];
  return (Number.isInteger(n) ? n : n.toFixed(1)) + l;
}
function ke() {
}
function Ml(n, e) {
  return n != n ? e == e : n !== e || n && typeof n == "object" || typeof n == "function";
}
const gt = typeof window < "u";
let De = gt ? () => window.performance.now() : () => Date.now(), wt = gt ? (n) => requestAnimationFrame(n) : ke;
const ie = /* @__PURE__ */ new Set();
function kt(n) {
  ie.forEach((e) => {
    e.c(n) || (ie.delete(e), e.f());
  }), ie.size !== 0 && wt(kt);
}
function Vl(n) {
  let e;
  return ie.size === 0 && wt(kt), {
    promise: new Promise((t) => {
      ie.add(e = { c: n, f: t });
    }),
    abort() {
      ie.delete(e);
    }
  };
}
const te = [];
function zl(n, e = ke) {
  let t;
  const l = /* @__PURE__ */ new Set();
  function i(a) {
    if (Ml(n, a) && (n = a, t)) {
      const r = !te.length;
      for (const f of l)
        f[1](), te.push(f, n);
      if (r) {
        for (let f = 0; f < te.length; f += 2)
          te[f][0](te[f + 1]);
        te.length = 0;
      }
    }
  }
  function s(a) {
    i(a(n));
  }
  function o(a, r = ke) {
    const f = [a, r];
    return l.add(f), l.size === 1 && (t = e(i, s) || ke), a(n), () => {
      l.delete(f), l.size === 0 && t && (t(), t = null);
    };
  }
  return { set: i, update: s, subscribe: o };
}
function He(n) {
  return Object.prototype.toString.call(n) === "[object Date]";
}
function Ve(n, e, t, l) {
  if (typeof t == "number" || He(t)) {
    const i = l - t, s = (t - e) / (n.dt || 1 / 60), o = n.opts.stiffness * i, a = n.opts.damping * s, r = (o - a) * n.inv_mass, f = (s + r) * n.dt;
    return Math.abs(f) < n.opts.precision && Math.abs(i) < n.opts.precision ? l : (n.settled = !1, He(t) ? new Date(t.getTime() + f) : t + f);
  } else {
    if (Array.isArray(t))
      return t.map(
        (i, s) => Ve(n, e[s], t[s], l[s])
      );
    if (typeof t == "object") {
      const i = {};
      for (const s in t)
        i[s] = Ve(n, e[s], t[s], l[s]);
      return i;
    } else
      throw new Error(`Cannot spring ${typeof t} values`);
  }
}
function Te(n, e = {}) {
  const t = zl(n), { stiffness: l = 0.15, damping: i = 0.8, precision: s = 0.01 } = e;
  let o, a, r, f = n, u = n, _ = 1, k = 0, m = !1;
  function p(y, L = {}) {
    u = y;
    const d = r = {};
    return n == null || L.hard || C.stiffness >= 1 && C.damping >= 1 ? (m = !0, o = De(), f = y, t.set(n = u), Promise.resolve()) : (L.soft && (k = 1 / ((L.soft === !0 ? 0.5 : +L.soft) * 60), _ = 0), a || (o = De(), m = !1, a = Vl((c) => {
      if (m)
        return m = !1, a = null, !1;
      _ = Math.min(_ + k, 1);
      const q = {
        inv_mass: _,
        opts: C,
        settled: !0,
        dt: (c - o) * 60 / 1e3
      }, z = Ve(q, f, n, u);
      return o = c, f = n, t.set(n = z), q.settled && (a = null), !q.settled;
    })), new Promise((c) => {
      a.promise.then(() => {
        d === r && c();
      });
    }));
  }
  const C = {
    set: p,
    update: (y, L) => p(y(u, n), L),
    subscribe: t.subscribe,
    stiffness: l,
    damping: i,
    precision: s
  };
  return C;
}
const {
  SvelteComponent: Nl,
  append: j,
  attr: v,
  component_subscribe: Re,
  detach: Al,
  element: El,
  init: jl,
  insert: Il,
  noop: Xe,
  safe_not_equal: Zl,
  set_style: ge,
  svg_element: I,
  toggle_class: Ye
} = window.__gradio__svelte__internal, { onMount: Pl } = window.__gradio__svelte__internal;
function Wl(n) {
  let e, t, l, i, s, o, a, r, f, u, _, k;
  return {
    c() {
      e = El("div"), t = I("svg"), l = I("g"), i = I("path"), s = I("path"), o = I("path"), a = I("path"), r = I("g"), f = I("path"), u = I("path"), _ = I("path"), k = I("path"), v(i, "d", "M255.926 0.754768L509.702 139.936V221.027L255.926 81.8465V0.754768Z"), v(i, "fill", "#FF7C00"), v(i, "fill-opacity", "0.4"), v(i, "class", "svelte-43sxxs"), v(s, "d", "M509.69 139.936L254.981 279.641V361.255L509.69 221.55V139.936Z"), v(s, "fill", "#FF7C00"), v(s, "class", "svelte-43sxxs"), v(o, "d", "M0.250138 139.937L254.981 279.641V361.255L0.250138 221.55V139.937Z"), v(o, "fill", "#FF7C00"), v(o, "fill-opacity", "0.4"), v(o, "class", "svelte-43sxxs"), v(a, "d", "M255.923 0.232622L0.236328 139.936V221.55L255.923 81.8469V0.232622Z"), v(a, "fill", "#FF7C00"), v(a, "class", "svelte-43sxxs"), ge(l, "transform", "translate(" + /*$top*/
      n[1][0] + "px, " + /*$top*/
      n[1][1] + "px)"), v(f, "d", "M255.926 141.5L509.702 280.681V361.773L255.926 222.592V141.5Z"), v(f, "fill", "#FF7C00"), v(f, "fill-opacity", "0.4"), v(f, "class", "svelte-43sxxs"), v(u, "d", "M509.69 280.679L254.981 420.384V501.998L509.69 362.293V280.679Z"), v(u, "fill", "#FF7C00"), v(u, "class", "svelte-43sxxs"), v(_, "d", "M0.250138 280.681L254.981 420.386V502L0.250138 362.295V280.681Z"), v(_, "fill", "#FF7C00"), v(_, "fill-opacity", "0.4"), v(_, "class", "svelte-43sxxs"), v(k, "d", "M255.923 140.977L0.236328 280.68V362.294L255.923 222.591V140.977Z"), v(k, "fill", "#FF7C00"), v(k, "class", "svelte-43sxxs"), ge(r, "transform", "translate(" + /*$bottom*/
      n[2][0] + "px, " + /*$bottom*/
      n[2][1] + "px)"), v(t, "viewBox", "-1200 -1200 3000 3000"), v(t, "fill", "none"), v(t, "xmlns", "http://www.w3.org/2000/svg"), v(t, "class", "svelte-43sxxs"), v(e, "class", "svelte-43sxxs"), Ye(
        e,
        "margin",
        /*margin*/
        n[0]
      );
    },
    m(m, p) {
      Il(m, e, p), j(e, t), j(t, l), j(l, i), j(l, s), j(l, o), j(l, a), j(t, r), j(r, f), j(r, u), j(r, _), j(r, k);
    },
    p(m, [p]) {
      p & /*$top*/
      2 && ge(l, "transform", "translate(" + /*$top*/
      m[1][0] + "px, " + /*$top*/
      m[1][1] + "px)"), p & /*$bottom*/
      4 && ge(r, "transform", "translate(" + /*$bottom*/
      m[2][0] + "px, " + /*$bottom*/
      m[2][1] + "px)"), p & /*margin*/
      1 && Ye(
        e,
        "margin",
        /*margin*/
        m[0]
      );
    },
    i: Xe,
    o: Xe,
    d(m) {
      m && Al(e);
    }
  };
}
function Bl(n, e, t) {
  let l, i;
  var s = this && this.__awaiter || function(m, p, C, y) {
    function L(d) {
      return d instanceof C ? d : new C(function(c) {
        c(d);
      });
    }
    return new (C || (C = Promise))(function(d, c) {
      function q(M) {
        try {
          h(y.next(M));
        } catch (T) {
          c(T);
        }
      }
      function z(M) {
        try {
          h(y.throw(M));
        } catch (T) {
          c(T);
        }
      }
      function h(M) {
        M.done ? d(M.value) : L(M.value).then(q, z);
      }
      h((y = y.apply(m, p || [])).next());
    });
  };
  let { margin: o = !0 } = e;
  const a = Te([0, 0]);
  Re(n, a, (m) => t(1, l = m));
  const r = Te([0, 0]);
  Re(n, r, (m) => t(2, i = m));
  let f;
  function u() {
    return s(this, void 0, void 0, function* () {
      yield Promise.all([a.set([125, 140]), r.set([-125, -140])]), yield Promise.all([a.set([-125, 140]), r.set([125, -140])]), yield Promise.all([a.set([-125, 0]), r.set([125, -0])]), yield Promise.all([a.set([125, 0]), r.set([-125, 0])]);
    });
  }
  function _() {
    return s(this, void 0, void 0, function* () {
      yield u(), f || _();
    });
  }
  function k() {
    return s(this, void 0, void 0, function* () {
      yield Promise.all([a.set([125, 0]), r.set([-125, 0])]), _();
    });
  }
  return Pl(() => (k(), () => f = !0)), n.$$set = (m) => {
    "margin" in m && t(0, o = m.margin);
  }, [o, l, i, a, r];
}
class Dl extends Nl {
  constructor(e) {
    super(), jl(this, e, Bl, Wl, Zl, { margin: 0 });
  }
}
const {
  SvelteComponent: Hl,
  append: J,
  attr: P,
  binding_callbacks: Ge,
  check_outros: pt,
  create_component: yt,
  create_slot: Tl,
  destroy_component: vt,
  destroy_each: qt,
  detach: g,
  element: H,
  empty: se,
  ensure_array_like: pe,
  get_all_dirty_from_scope: Rl,
  get_slot_changes: Xl,
  group_outros: Ct,
  init: Yl,
  insert: w,
  mount_component: Ft,
  noop: ze,
  safe_not_equal: Gl,
  set_data: A,
  set_style: Y,
  space: W,
  text: F,
  toggle_class: N,
  transition_in: K,
  transition_out: Q,
  update_slot_base: Ol
} = window.__gradio__svelte__internal, { tick: Ul } = window.__gradio__svelte__internal, { onDestroy: Jl } = window.__gradio__svelte__internal, { createEventDispatcher: Kl } = window.__gradio__svelte__internal, Ql = (n) => ({}), Oe = (n) => ({});
function Ue(n, e, t) {
  const l = n.slice();
  return l[41] = e[t], l[43] = t, l;
}
function Je(n, e, t) {
  const l = n.slice();
  return l[41] = e[t], l;
}
function xl(n) {
  let e, t, l, i, s = (
    /*i18n*/
    n[1]("common.error") + ""
  ), o, a, r;
  t = new kl({
    props: {
      Icon: Ll,
      label: (
        /*i18n*/
        n[1]("common.clear")
      ),
      disabled: !1
    }
  }), t.$on(
    "click",
    /*click_handler*/
    n[32]
  );
  const f = (
    /*#slots*/
    n[30].error
  ), u = Tl(
    f,
    n,
    /*$$scope*/
    n[29],
    Oe
  );
  return {
    c() {
      e = H("div"), yt(t.$$.fragment), l = W(), i = H("span"), o = F(s), a = W(), u && u.c(), P(e, "class", "clear-status svelte-1yk38uw"), P(i, "class", "error svelte-1yk38uw");
    },
    m(_, k) {
      w(_, e, k), Ft(t, e, null), w(_, l, k), w(_, i, k), J(i, o), w(_, a, k), u && u.m(_, k), r = !0;
    },
    p(_, k) {
      const m = {};
      k[0] & /*i18n*/
      2 && (m.label = /*i18n*/
      _[1]("common.clear")), t.$set(m), (!r || k[0] & /*i18n*/
      2) && s !== (s = /*i18n*/
      _[1]("common.error") + "") && A(o, s), u && u.p && (!r || k[0] & /*$$scope*/
      536870912) && Ol(
        u,
        f,
        _,
        /*$$scope*/
        _[29],
        r ? Xl(
          f,
          /*$$scope*/
          _[29],
          k,
          Ql
        ) : Rl(
          /*$$scope*/
          _[29]
        ),
        Oe
      );
    },
    i(_) {
      r || (K(t.$$.fragment, _), K(u, _), r = !0);
    },
    o(_) {
      Q(t.$$.fragment, _), Q(u, _), r = !1;
    },
    d(_) {
      _ && (g(e), g(l), g(i), g(a)), vt(t), u && u.d(_);
    }
  };
}
function $l(n) {
  let e, t, l, i, s, o, a, r, f, u = (
    /*variant*/
    n[8] === "default" && /*show_eta_bar*/
    n[18] && /*show_progress*/
    n[6] === "full" && Ke(n)
  );
  function _(c, q) {
    if (
      /*progress*/
      c[7]
    )
      return ln;
    if (
      /*queue_position*/
      c[2] !== null && /*queue_size*/
      c[3] !== void 0 && /*queue_position*/
      c[2] >= 0
    )
      return tn;
    if (
      /*queue_position*/
      c[2] === 0
    )
      return en;
  }
  let k = _(n), m = k && k(n), p = (
    /*timer*/
    n[5] && $e(n)
  );
  const C = [on, fn], y = [];
  function L(c, q) {
    return (
      /*last_progress_level*/
      c[15] != null ? 0 : (
        /*show_progress*/
        c[6] === "full" ? 1 : -1
      )
    );
  }
  ~(s = L(n)) && (o = y[s] = C[s](n));
  let d = !/*timer*/
  n[5] && ft(n);
  return {
    c() {
      u && u.c(), e = W(), t = H("div"), m && m.c(), l = W(), p && p.c(), i = W(), o && o.c(), a = W(), d && d.c(), r = se(), P(t, "class", "progress-text svelte-1yk38uw"), N(
        t,
        "meta-text-center",
        /*variant*/
        n[8] === "center"
      ), N(
        t,
        "meta-text",
        /*variant*/
        n[8] === "default"
      );
    },
    m(c, q) {
      u && u.m(c, q), w(c, e, q), w(c, t, q), m && m.m(t, null), J(t, l), p && p.m(t, null), w(c, i, q), ~s && y[s].m(c, q), w(c, a, q), d && d.m(c, q), w(c, r, q), f = !0;
    },
    p(c, q) {
      /*variant*/
      c[8] === "default" && /*show_eta_bar*/
      c[18] && /*show_progress*/
      c[6] === "full" ? u ? u.p(c, q) : (u = Ke(c), u.c(), u.m(e.parentNode, e)) : u && (u.d(1), u = null), k === (k = _(c)) && m ? m.p(c, q) : (m && m.d(1), m = k && k(c), m && (m.c(), m.m(t, l))), /*timer*/
      c[5] ? p ? p.p(c, q) : (p = $e(c), p.c(), p.m(t, null)) : p && (p.d(1), p = null), (!f || q[0] & /*variant*/
      256) && N(
        t,
        "meta-text-center",
        /*variant*/
        c[8] === "center"
      ), (!f || q[0] & /*variant*/
      256) && N(
        t,
        "meta-text",
        /*variant*/
        c[8] === "default"
      );
      let z = s;
      s = L(c), s === z ? ~s && y[s].p(c, q) : (o && (Ct(), Q(y[z], 1, 1, () => {
        y[z] = null;
      }), pt()), ~s ? (o = y[s], o ? o.p(c, q) : (o = y[s] = C[s](c), o.c()), K(o, 1), o.m(a.parentNode, a)) : o = null), /*timer*/
      c[5] ? d && (d.d(1), d = null) : d ? d.p(c, q) : (d = ft(c), d.c(), d.m(r.parentNode, r));
    },
    i(c) {
      f || (K(o), f = !0);
    },
    o(c) {
      Q(o), f = !1;
    },
    d(c) {
      c && (g(e), g(t), g(i), g(a), g(r)), u && u.d(c), m && m.d(), p && p.d(), ~s && y[s].d(c), d && d.d(c);
    }
  };
}
function Ke(n) {
  let e, t = `translateX(${/*eta_level*/
  (n[17] || 0) * 100 - 100}%)`;
  return {
    c() {
      e = H("div"), P(e, "class", "eta-bar svelte-1yk38uw"), Y(e, "transform", t);
    },
    m(l, i) {
      w(l, e, i);
    },
    p(l, i) {
      i[0] & /*eta_level*/
      131072 && t !== (t = `translateX(${/*eta_level*/
      (l[17] || 0) * 100 - 100}%)`) && Y(e, "transform", t);
    },
    d(l) {
      l && g(e);
    }
  };
}
function en(n) {
  let e;
  return {
    c() {
      e = F("processing |");
    },
    m(t, l) {
      w(t, e, l);
    },
    p: ze,
    d(t) {
      t && g(e);
    }
  };
}
function tn(n) {
  let e, t = (
    /*queue_position*/
    n[2] + 1 + ""
  ), l, i, s, o;
  return {
    c() {
      e = F("queue: "), l = F(t), i = F("/"), s = F(
        /*queue_size*/
        n[3]
      ), o = F(" |");
    },
    m(a, r) {
      w(a, e, r), w(a, l, r), w(a, i, r), w(a, s, r), w(a, o, r);
    },
    p(a, r) {
      r[0] & /*queue_position*/
      4 && t !== (t = /*queue_position*/
      a[2] + 1 + "") && A(l, t), r[0] & /*queue_size*/
      8 && A(
        s,
        /*queue_size*/
        a[3]
      );
    },
    d(a) {
      a && (g(e), g(l), g(i), g(s), g(o));
    }
  };
}
function ln(n) {
  let e, t = pe(
    /*progress*/
    n[7]
  ), l = [];
  for (let i = 0; i < t.length; i += 1)
    l[i] = xe(Je(n, t, i));
  return {
    c() {
      for (let i = 0; i < l.length; i += 1)
        l[i].c();
      e = se();
    },
    m(i, s) {
      for (let o = 0; o < l.length; o += 1)
        l[o] && l[o].m(i, s);
      w(i, e, s);
    },
    p(i, s) {
      if (s[0] & /*progress*/
      128) {
        t = pe(
          /*progress*/
          i[7]
        );
        let o;
        for (o = 0; o < t.length; o += 1) {
          const a = Je(i, t, o);
          l[o] ? l[o].p(a, s) : (l[o] = xe(a), l[o].c(), l[o].m(e.parentNode, e));
        }
        for (; o < l.length; o += 1)
          l[o].d(1);
        l.length = t.length;
      }
    },
    d(i) {
      i && g(e), qt(l, i);
    }
  };
}
function Qe(n) {
  let e, t = (
    /*p*/
    n[41].unit + ""
  ), l, i, s = " ", o;
  function a(u, _) {
    return (
      /*p*/
      u[41].length != null ? sn : nn
    );
  }
  let r = a(n), f = r(n);
  return {
    c() {
      f.c(), e = W(), l = F(t), i = F(" | "), o = F(s);
    },
    m(u, _) {
      f.m(u, _), w(u, e, _), w(u, l, _), w(u, i, _), w(u, o, _);
    },
    p(u, _) {
      r === (r = a(u)) && f ? f.p(u, _) : (f.d(1), f = r(u), f && (f.c(), f.m(e.parentNode, e))), _[0] & /*progress*/
      128 && t !== (t = /*p*/
      u[41].unit + "") && A(l, t);
    },
    d(u) {
      u && (g(e), g(l), g(i), g(o)), f.d(u);
    }
  };
}
function nn(n) {
  let e = ne(
    /*p*/
    n[41].index || 0
  ) + "", t;
  return {
    c() {
      t = F(e);
    },
    m(l, i) {
      w(l, t, i);
    },
    p(l, i) {
      i[0] & /*progress*/
      128 && e !== (e = ne(
        /*p*/
        l[41].index || 0
      ) + "") && A(t, e);
    },
    d(l) {
      l && g(t);
    }
  };
}
function sn(n) {
  let e = ne(
    /*p*/
    n[41].index || 0
  ) + "", t, l, i = ne(
    /*p*/
    n[41].length
  ) + "", s;
  return {
    c() {
      t = F(e), l = F("/"), s = F(i);
    },
    m(o, a) {
      w(o, t, a), w(o, l, a), w(o, s, a);
    },
    p(o, a) {
      a[0] & /*progress*/
      128 && e !== (e = ne(
        /*p*/
        o[41].index || 0
      ) + "") && A(t, e), a[0] & /*progress*/
      128 && i !== (i = ne(
        /*p*/
        o[41].length
      ) + "") && A(s, i);
    },
    d(o) {
      o && (g(t), g(l), g(s));
    }
  };
}
function xe(n) {
  let e, t = (
    /*p*/
    n[41].index != null && Qe(n)
  );
  return {
    c() {
      t && t.c(), e = se();
    },
    m(l, i) {
      t && t.m(l, i), w(l, e, i);
    },
    p(l, i) {
      /*p*/
      l[41].index != null ? t ? t.p(l, i) : (t = Qe(l), t.c(), t.m(e.parentNode, e)) : t && (t.d(1), t = null);
    },
    d(l) {
      l && g(e), t && t.d(l);
    }
  };
}
function $e(n) {
  let e, t = (
    /*eta*/
    n[0] ? `/${/*formatted_eta*/
    n[19]}` : ""
  ), l, i;
  return {
    c() {
      e = F(
        /*formatted_timer*/
        n[20]
      ), l = F(t), i = F("s");
    },
    m(s, o) {
      w(s, e, o), w(s, l, o), w(s, i, o);
    },
    p(s, o) {
      o[0] & /*formatted_timer*/
      1048576 && A(
        e,
        /*formatted_timer*/
        s[20]
      ), o[0] & /*eta, formatted_eta*/
      524289 && t !== (t = /*eta*/
      s[0] ? `/${/*formatted_eta*/
      s[19]}` : "") && A(l, t);
    },
    d(s) {
      s && (g(e), g(l), g(i));
    }
  };
}
function fn(n) {
  let e, t;
  return e = new Dl({
    props: { margin: (
      /*variant*/
      n[8] === "default"
    ) }
  }), {
    c() {
      yt(e.$$.fragment);
    },
    m(l, i) {
      Ft(e, l, i), t = !0;
    },
    p(l, i) {
      const s = {};
      i[0] & /*variant*/
      256 && (s.margin = /*variant*/
      l[8] === "default"), e.$set(s);
    },
    i(l) {
      t || (K(e.$$.fragment, l), t = !0);
    },
    o(l) {
      Q(e.$$.fragment, l), t = !1;
    },
    d(l) {
      vt(e, l);
    }
  };
}
function on(n) {
  let e, t, l, i, s, o = `${/*last_progress_level*/
  n[15] * 100}%`, a = (
    /*progress*/
    n[7] != null && et(n)
  );
  return {
    c() {
      e = H("div"), t = H("div"), a && a.c(), l = W(), i = H("div"), s = H("div"), P(t, "class", "progress-level-inner svelte-1yk38uw"), P(s, "class", "progress-bar svelte-1yk38uw"), Y(s, "width", o), P(i, "class", "progress-bar-wrap svelte-1yk38uw"), P(e, "class", "progress-level svelte-1yk38uw");
    },
    m(r, f) {
      w(r, e, f), J(e, t), a && a.m(t, null), J(e, l), J(e, i), J(i, s), n[31](s);
    },
    p(r, f) {
      /*progress*/
      r[7] != null ? a ? a.p(r, f) : (a = et(r), a.c(), a.m(t, null)) : a && (a.d(1), a = null), f[0] & /*last_progress_level*/
      32768 && o !== (o = `${/*last_progress_level*/
      r[15] * 100}%`) && Y(s, "width", o);
    },
    i: ze,
    o: ze,
    d(r) {
      r && g(e), a && a.d(), n[31](null);
    }
  };
}
function et(n) {
  let e, t = pe(
    /*progress*/
    n[7]
  ), l = [];
  for (let i = 0; i < t.length; i += 1)
    l[i] = st(Ue(n, t, i));
  return {
    c() {
      for (let i = 0; i < l.length; i += 1)
        l[i].c();
      e = se();
    },
    m(i, s) {
      for (let o = 0; o < l.length; o += 1)
        l[o] && l[o].m(i, s);
      w(i, e, s);
    },
    p(i, s) {
      if (s[0] & /*progress_level, progress*/
      16512) {
        t = pe(
          /*progress*/
          i[7]
        );
        let o;
        for (o = 0; o < t.length; o += 1) {
          const a = Ue(i, t, o);
          l[o] ? l[o].p(a, s) : (l[o] = st(a), l[o].c(), l[o].m(e.parentNode, e));
        }
        for (; o < l.length; o += 1)
          l[o].d(1);
        l.length = t.length;
      }
    },
    d(i) {
      i && g(e), qt(l, i);
    }
  };
}
function tt(n) {
  let e, t, l, i, s = (
    /*i*/
    n[43] !== 0 && rn()
  ), o = (
    /*p*/
    n[41].desc != null && lt(n)
  ), a = (
    /*p*/
    n[41].desc != null && /*progress_level*/
    n[14] && /*progress_level*/
    n[14][
      /*i*/
      n[43]
    ] != null && nt()
  ), r = (
    /*progress_level*/
    n[14] != null && it(n)
  );
  return {
    c() {
      s && s.c(), e = W(), o && o.c(), t = W(), a && a.c(), l = W(), r && r.c(), i = se();
    },
    m(f, u) {
      s && s.m(f, u), w(f, e, u), o && o.m(f, u), w(f, t, u), a && a.m(f, u), w(f, l, u), r && r.m(f, u), w(f, i, u);
    },
    p(f, u) {
      /*p*/
      f[41].desc != null ? o ? o.p(f, u) : (o = lt(f), o.c(), o.m(t.parentNode, t)) : o && (o.d(1), o = null), /*p*/
      f[41].desc != null && /*progress_level*/
      f[14] && /*progress_level*/
      f[14][
        /*i*/
        f[43]
      ] != null ? a || (a = nt(), a.c(), a.m(l.parentNode, l)) : a && (a.d(1), a = null), /*progress_level*/
      f[14] != null ? r ? r.p(f, u) : (r = it(f), r.c(), r.m(i.parentNode, i)) : r && (r.d(1), r = null);
    },
    d(f) {
      f && (g(e), g(t), g(l), g(i)), s && s.d(f), o && o.d(f), a && a.d(f), r && r.d(f);
    }
  };
}
function rn(n) {
  let e;
  return {
    c() {
      e = F(" /");
    },
    m(t, l) {
      w(t, e, l);
    },
    d(t) {
      t && g(e);
    }
  };
}
function lt(n) {
  let e = (
    /*p*/
    n[41].desc + ""
  ), t;
  return {
    c() {
      t = F(e);
    },
    m(l, i) {
      w(l, t, i);
    },
    p(l, i) {
      i[0] & /*progress*/
      128 && e !== (e = /*p*/
      l[41].desc + "") && A(t, e);
    },
    d(l) {
      l && g(t);
    }
  };
}
function nt(n) {
  let e;
  return {
    c() {
      e = F("-");
    },
    m(t, l) {
      w(t, e, l);
    },
    d(t) {
      t && g(e);
    }
  };
}
function it(n) {
  let e = (100 * /*progress_level*/
  (n[14][
    /*i*/
    n[43]
  ] || 0)).toFixed(1) + "", t, l;
  return {
    c() {
      t = F(e), l = F("%");
    },
    m(i, s) {
      w(i, t, s), w(i, l, s);
    },
    p(i, s) {
      s[0] & /*progress_level*/
      16384 && e !== (e = (100 * /*progress_level*/
      (i[14][
        /*i*/
        i[43]
      ] || 0)).toFixed(1) + "") && A(t, e);
    },
    d(i) {
      i && (g(t), g(l));
    }
  };
}
function st(n) {
  let e, t = (
    /*p*/
    (n[41].desc != null || /*progress_level*/
    n[14] && /*progress_level*/
    n[14][
      /*i*/
      n[43]
    ] != null) && tt(n)
  );
  return {
    c() {
      t && t.c(), e = se();
    },
    m(l, i) {
      t && t.m(l, i), w(l, e, i);
    },
    p(l, i) {
      /*p*/
      l[41].desc != null || /*progress_level*/
      l[14] && /*progress_level*/
      l[14][
        /*i*/
        l[43]
      ] != null ? t ? t.p(l, i) : (t = tt(l), t.c(), t.m(e.parentNode, e)) : t && (t.d(1), t = null);
    },
    d(l) {
      l && g(e), t && t.d(l);
    }
  };
}
function ft(n) {
  let e, t;
  return {
    c() {
      e = H("p"), t = F(
        /*loading_text*/
        n[9]
      ), P(e, "class", "loading svelte-1yk38uw");
    },
    m(l, i) {
      w(l, e, i), J(e, t);
    },
    p(l, i) {
      i[0] & /*loading_text*/
      512 && A(
        t,
        /*loading_text*/
        l[9]
      );
    },
    d(l) {
      l && g(e);
    }
  };
}
function an(n) {
  let e, t, l, i, s;
  const o = [$l, xl], a = [];
  function r(f, u) {
    return (
      /*status*/
      f[4] === "pending" ? 0 : (
        /*status*/
        f[4] === "error" ? 1 : -1
      )
    );
  }
  return ~(t = r(n)) && (l = a[t] = o[t](n)), {
    c() {
      e = H("div"), l && l.c(), P(e, "class", i = "wrap " + /*variant*/
      n[8] + " " + /*show_progress*/
      n[6] + " svelte-1yk38uw"), N(e, "hide", !/*status*/
      n[4] || /*status*/
      n[4] === "complete" || /*show_progress*/
      n[6] === "hidden"), N(
        e,
        "translucent",
        /*variant*/
        n[8] === "center" && /*status*/
        (n[4] === "pending" || /*status*/
        n[4] === "error") || /*translucent*/
        n[11] || /*show_progress*/
        n[6] === "minimal"
      ), N(
        e,
        "generating",
        /*status*/
        n[4] === "generating"
      ), N(
        e,
        "border",
        /*border*/
        n[12]
      ), Y(
        e,
        "position",
        /*absolute*/
        n[10] ? "absolute" : "static"
      ), Y(
        e,
        "padding",
        /*absolute*/
        n[10] ? "0" : "var(--size-8) 0"
      );
    },
    m(f, u) {
      w(f, e, u), ~t && a[t].m(e, null), n[33](e), s = !0;
    },
    p(f, u) {
      let _ = t;
      t = r(f), t === _ ? ~t && a[t].p(f, u) : (l && (Ct(), Q(a[_], 1, 1, () => {
        a[_] = null;
      }), pt()), ~t ? (l = a[t], l ? l.p(f, u) : (l = a[t] = o[t](f), l.c()), K(l, 1), l.m(e, null)) : l = null), (!s || u[0] & /*variant, show_progress*/
      320 && i !== (i = "wrap " + /*variant*/
      f[8] + " " + /*show_progress*/
      f[6] + " svelte-1yk38uw")) && P(e, "class", i), (!s || u[0] & /*variant, show_progress, status, show_progress*/
      336) && N(e, "hide", !/*status*/
      f[4] || /*status*/
      f[4] === "complete" || /*show_progress*/
      f[6] === "hidden"), (!s || u[0] & /*variant, show_progress, variant, status, translucent, show_progress*/
      2384) && N(
        e,
        "translucent",
        /*variant*/
        f[8] === "center" && /*status*/
        (f[4] === "pending" || /*status*/
        f[4] === "error") || /*translucent*/
        f[11] || /*show_progress*/
        f[6] === "minimal"
      ), (!s || u[0] & /*variant, show_progress, status*/
      336) && N(
        e,
        "generating",
        /*status*/
        f[4] === "generating"
      ), (!s || u[0] & /*variant, show_progress, border*/
      4416) && N(
        e,
        "border",
        /*border*/
        f[12]
      ), u[0] & /*absolute*/
      1024 && Y(
        e,
        "position",
        /*absolute*/
        f[10] ? "absolute" : "static"
      ), u[0] & /*absolute*/
      1024 && Y(
        e,
        "padding",
        /*absolute*/
        f[10] ? "0" : "var(--size-8) 0"
      );
    },
    i(f) {
      s || (K(l), s = !0);
    },
    o(f) {
      Q(l), s = !1;
    },
    d(f) {
      f && g(e), ~t && a[t].d(), n[33](null);
    }
  };
}
var un = function(n, e, t, l) {
  function i(s) {
    return s instanceof t ? s : new t(function(o) {
      o(s);
    });
  }
  return new (t || (t = Promise))(function(s, o) {
    function a(u) {
      try {
        f(l.next(u));
      } catch (_) {
        o(_);
      }
    }
    function r(u) {
      try {
        f(l.throw(u));
      } catch (_) {
        o(_);
      }
    }
    function f(u) {
      u.done ? s(u.value) : i(u.value).then(a, r);
    }
    f((l = l.apply(n, e || [])).next());
  });
};
let we = [], Le = !1;
function cn(n) {
  return un(this, arguments, void 0, function* (e, t = !0) {
    if (!(window.__gradio_mode__ === "website" || window.__gradio_mode__ !== "app" && t !== !0)) {
      if (we.push(e), !Le)
        Le = !0;
      else
        return;
      yield Ul(), requestAnimationFrame(() => {
        let l = [0, 0];
        for (let i = 0; i < we.length; i++) {
          const o = we[i].getBoundingClientRect();
          (i === 0 || o.top + window.scrollY <= l[0]) && (l[0] = o.top + window.scrollY, l[1] = i);
        }
        window.scrollTo({ top: l[0] - 20, behavior: "smooth" }), Le = !1, we = [];
      });
    }
  });
}
function _n(n, e, t) {
  let l, { $$slots: i = {}, $$scope: s } = e;
  this && this.__awaiter;
  const o = Kl();
  let { i18n: a } = e, { eta: r = null } = e, { queue_position: f } = e, { queue_size: u } = e, { status: _ } = e, { scroll_to_output: k = !1 } = e, { timer: m = !0 } = e, { show_progress: p = "full" } = e, { message: C = null } = e, { progress: y = null } = e, { variant: L = "default" } = e, { loading_text: d = "Loading..." } = e, { absolute: c = !0 } = e, { translucent: q = !1 } = e, { border: z = !1 } = e, { autoscroll: h } = e, M, T = !1, ue = 0, G = 0, x = null, $ = null, Ee = 0, O = null, fe, X = null, je = !0;
  const Nt = () => {
    t(0, r = t(27, x = t(19, ce = null))), t(25, ue = performance.now()), t(26, G = 0), T = !0, Ie();
  };
  function Ie() {
    requestAnimationFrame(() => {
      t(26, G = (performance.now() - ue) / 1e3), T && Ie();
    });
  }
  function Ze() {
    t(26, G = 0), t(0, r = t(27, x = t(19, ce = null))), T && (T = !1);
  }
  Jl(() => {
    T && Ze();
  });
  let ce = null;
  function At(b) {
    Ge[b ? "unshift" : "push"](() => {
      X = b, t(16, X), t(7, y), t(14, O), t(15, fe);
    });
  }
  const Et = () => {
    o("clear_status");
  };
  function jt(b) {
    Ge[b ? "unshift" : "push"](() => {
      M = b, t(13, M);
    });
  }
  return n.$$set = (b) => {
    "i18n" in b && t(1, a = b.i18n), "eta" in b && t(0, r = b.eta), "queue_position" in b && t(2, f = b.queue_position), "queue_size" in b && t(3, u = b.queue_size), "status" in b && t(4, _ = b.status), "scroll_to_output" in b && t(22, k = b.scroll_to_output), "timer" in b && t(5, m = b.timer), "show_progress" in b && t(6, p = b.show_progress), "message" in b && t(23, C = b.message), "progress" in b && t(7, y = b.progress), "variant" in b && t(8, L = b.variant), "loading_text" in b && t(9, d = b.loading_text), "absolute" in b && t(10, c = b.absolute), "translucent" in b && t(11, q = b.translucent), "border" in b && t(12, z = b.border), "autoscroll" in b && t(24, h = b.autoscroll), "$$scope" in b && t(29, s = b.$$scope);
  }, n.$$.update = () => {
    n.$$.dirty[0] & /*eta, old_eta, timer_start, eta_from_start*/
    436207617 && (r === null && t(0, r = x), r != null && x !== r && (t(28, $ = (performance.now() - ue) / 1e3 + r), t(19, ce = $.toFixed(1)), t(27, x = r))), n.$$.dirty[0] & /*eta_from_start, timer_diff*/
    335544320 && t(17, Ee = $ === null || $ <= 0 || !G ? null : Math.min(G / $, 1)), n.$$.dirty[0] & /*progress*/
    128 && y != null && t(18, je = !1), n.$$.dirty[0] & /*progress, progress_level, progress_bar, last_progress_level*/
    114816 && (y != null ? t(14, O = y.map((b) => {
      if (b.index != null && b.length != null)
        return b.index / b.length;
      if (b.progress != null)
        return b.progress;
    })) : t(14, O = null), O ? (t(15, fe = O[O.length - 1]), X && (fe === 0 ? t(16, X.style.transition = "0", X) : t(16, X.style.transition = "150ms", X))) : t(15, fe = void 0)), n.$$.dirty[0] & /*status*/
    16 && (_ === "pending" ? Nt() : Ze()), n.$$.dirty[0] & /*el, scroll_to_output, status, autoscroll*/
    20979728 && M && k && (_ === "pending" || _ === "complete") && cn(M, h), n.$$.dirty[0] & /*status, message*/
    8388624, n.$$.dirty[0] & /*timer_diff*/
    67108864 && t(20, l = G.toFixed(1));
  }, [
    r,
    a,
    f,
    u,
    _,
    m,
    p,
    y,
    L,
    d,
    c,
    q,
    z,
    M,
    O,
    fe,
    X,
    Ee,
    je,
    ce,
    l,
    o,
    k,
    C,
    h,
    ue,
    G,
    x,
    $,
    s,
    i,
    At,
    Et,
    jt
  ];
}
class dn extends Hl {
  constructor(e) {
    super(), Yl(
      this,
      e,
      _n,
      an,
      Gl,
      {
        i18n: 1,
        eta: 0,
        queue_position: 2,
        queue_size: 3,
        status: 4,
        scroll_to_output: 22,
        timer: 5,
        show_progress: 6,
        message: 23,
        progress: 7,
        variant: 8,
        loading_text: 9,
        absolute: 10,
        translucent: 11,
        border: 12,
        autoscroll: 24
      },
      null,
      [-1, -1]
    );
  }
}
const {
  SvelteComponent: mn,
  append: bn,
  attr: re,
  detach: Lt,
  element: ot,
  empty: hn,
  init: gn,
  insert: St,
  noop: rt,
  safe_not_equal: wn,
  src_url_equal: at,
  toggle_class: le
} = window.__gradio__svelte__internal;
function ut(n) {
  let e, t, l;
  return {
    c() {
      e = ot("div"), t = ot("img"), at(t.src, l = /*value*/
      n[0].url) || re(t, "src", l), re(t, "alt", ""), re(t, "class", "svelte-giydt1"), re(e, "class", "container svelte-giydt1"), le(
        e,
        "table",
        /*type*/
        n[1] === "table"
      ), le(
        e,
        "gallery",
        /*type*/
        n[1] === "gallery"
      ), le(
        e,
        "selected",
        /*selected*/
        n[2]
      );
    },
    m(i, s) {
      St(i, e, s), bn(e, t);
    },
    p(i, s) {
      s & /*value*/
      1 && !at(t.src, l = /*value*/
      i[0].url) && re(t, "src", l), s & /*type*/
      2 && le(
        e,
        "table",
        /*type*/
        i[1] === "table"
      ), s & /*type*/
      2 && le(
        e,
        "gallery",
        /*type*/
        i[1] === "gallery"
      ), s & /*selected*/
      4 && le(
        e,
        "selected",
        /*selected*/
        i[2]
      );
    },
    d(i) {
      i && Lt(e);
    }
  };
}
function kn(n) {
  let e, t = (
    /*value*/
    n[0] && ut(n)
  );
  return {
    c() {
      t && t.c(), e = hn();
    },
    m(l, i) {
      t && t.m(l, i), St(l, e, i);
    },
    p(l, [i]) {
      /*value*/
      l[0] ? t ? t.p(l, i) : (t = ut(l), t.c(), t.m(e.parentNode, e)) : t && (t.d(1), t = null);
    },
    i: rt,
    o: rt,
    d(l) {
      l && Lt(e), t && t.d(l);
    }
  };
}
function pn(n, e, t) {
  let { value: l } = e, { type: i } = e, { selected: s = !1 } = e;
  return n.$$set = (o) => {
    "value" in o && t(0, l = o.value), "type" in o && t(1, i = o.type), "selected" in o && t(2, s = o.selected);
  }, [l, i, s];
}
class Wn extends mn {
  constructor(e) {
    super(), gn(this, e, pn, kn, wn, { value: 0, type: 1, selected: 2 });
  }
}
const {
  SvelteComponent: yn,
  assign: vn,
  attr: qn,
  binding_callbacks: Cn,
  check_outros: Fn,
  create_component: Mt,
  destroy_component: Vt,
  detach: Ne,
  element: Ln,
  empty: Sn,
  flush: Z,
  get_spread_object: Mn,
  get_spread_update: Vn,
  group_outros: zn,
  init: Nn,
  insert: Ae,
  mount_component: zt,
  safe_not_equal: An,
  set_style: ct,
  space: En,
  transition_in: ae,
  transition_out: ye
} = window.__gradio__svelte__internal, { onMount: jn } = window.__gradio__svelte__internal;
function _t(n) {
  let e, t;
  return e = new nl({
    props: {
      visible: (
        /*visible*/
        n[3]
      ),
      variant: "solid",
      border_mode: (
        /*dragging*/
        n[11] ? "focus" : "base"
      ),
      padding: !1,
      elem_id: (
        /*elem_id*/
        n[1]
      ),
      elem_classes: (
        /*elem_classes*/
        n[2]
      ),
      allow_overflow: !1,
      container: (
        /*container*/
        n[4]
      ),
      scale: (
        /*scale*/
        n[5]
      ),
      min_width: (
        /*min_width*/
        n[6]
      ),
      $$slots: { default: [In] },
      $$scope: { ctx: n }
    }
  }), {
    c() {
      Mt(e.$$.fragment);
    },
    m(l, i) {
      zt(e, l, i), t = !0;
    },
    p(l, i) {
      const s = {};
      i & /*visible*/
      8 && (s.visible = /*visible*/
      l[3]), i & /*elem_id*/
      2 && (s.elem_id = /*elem_id*/
      l[1]), i & /*elem_classes*/
      4 && (s.elem_classes = /*elem_classes*/
      l[2]), i & /*container*/
      16 && (s.container = /*container*/
      l[4]), i & /*scale*/
      32 && (s.scale = /*scale*/
      l[5]), i & /*min_width*/
      64 && (s.min_width = /*min_width*/
      l[6]), i & /*$$scope, ref, height, gradio, loading_status*/
      67201 && (s.$$scope = { dirty: i, ctx: l }), e.$set(s);
    },
    i(l) {
      t || (ae(e.$$.fragment, l), t = !0);
    },
    o(l) {
      ye(e.$$.fragment, l), t = !1;
    },
    d(l) {
      Vt(e, l);
    }
  };
}
function In(n) {
  let e, t, l, i;
  const s = [
    { autoscroll: (
      /*gradio*/
      n[9].autoscroll
    ) },
    { i18n: (
      /*gradio*/
      n[9].i18n
    ) },
    /*loading_status*/
    n[7]
  ];
  let o = {};
  for (let a = 0; a < s.length; a += 1)
    o = vn(o, s[a]);
  return e = new dn({ props: o }), e.$on(
    "clear_status",
    /*clear_status_handler*/
    n[14]
  ), {
    c() {
      Mt(e.$$.fragment), t = En(), l = Ln("div"), qn(l, "class", "viewer svelte-gu2pck"), ct(
        l,
        "height",
        /*height*/
        n[0]
      );
    },
    m(a, r) {
      zt(e, a, r), Ae(a, t, r), Ae(a, l, r), n[15](l), i = !0;
    },
    p(a, r) {
      const f = r & /*gradio, loading_status*/
      640 ? Vn(s, [
        r & /*gradio*/
        512 && { autoscroll: (
          /*gradio*/
          a[9].autoscroll
        ) },
        r & /*gradio*/
        512 && { i18n: (
          /*gradio*/
          a[9].i18n
        ) },
        r & /*loading_status*/
        128 && Mn(
          /*loading_status*/
          a[7]
        )
      ]) : {};
      e.$set(f), r & /*height*/
      1 && ct(
        l,
        "height",
        /*height*/
        a[0]
      );
    },
    i(a) {
      i || (ae(e.$$.fragment, a), i = !0);
    },
    o(a) {
      ye(e.$$.fragment, a), i = !1;
    },
    d(a) {
      a && (Ne(t), Ne(l)), Vt(e, a), n[15](null);
    }
  };
}
function Zn(n) {
  let e, t, l = !/*interactive*/
  n[8] && _t(n);
  return {
    c() {
      l && l.c(), e = Sn();
    },
    m(i, s) {
      l && l.m(i, s), Ae(i, e, s), t = !0;
    },
    p(i, [s]) {
      /*interactive*/
      i[8] ? l && (zn(), ye(l, 1, 1, () => {
        l = null;
      }), Fn()) : l ? (l.p(i, s), s & /*interactive*/
      256 && ae(l, 1)) : (l = _t(i), l.c(), ae(l, 1), l.m(e.parentNode, e));
    },
    i(i) {
      t || (ae(l), t = !0);
    },
    o(i) {
      ye(l), t = !1;
    },
    d(i) {
      i && Ne(e), l && l.d(i);
    }
  };
}
function Pn(n, e, t) {
  let { elem_id: l = "" } = e, { elem_classes: i = [] } = e, { visible: s = !0 } = e, { height: o = 640 } = e, { value: a = null } = e, { container: r = !0 } = e, { scale: f = null } = e, { min_width: u = void 0 } = e, { loading_status: _ } = e, { interactive: k } = e, { gradio: m } = e, p, C, y;
  jn(() => (t(13, C = new Ht()), C.start(void 0, y), () => C.stop()));
  const L = () => m.dispatch("clear_status", _);
  function d(c) {
    Cn[c ? "unshift" : "push"](() => {
      y = c, t(10, y);
    });
  }
  return n.$$set = (c) => {
    "elem_id" in c && t(1, l = c.elem_id), "elem_classes" in c && t(2, i = c.elem_classes), "visible" in c && t(3, s = c.visible), "height" in c && t(0, o = c.height), "value" in c && t(12, a = c.value), "container" in c && t(4, r = c.container), "scale" in c && t(5, f = c.scale), "min_width" in c && t(6, u = c.min_width), "loading_status" in c && t(7, _ = c.loading_status), "interactive" in c && t(8, k = c.interactive), "gradio" in c && t(9, m = c.gradio);
  }, n.$$.update = () => {
    if (n.$$.dirty & /*height*/
    1 && t(0, o = typeof o == "number" ? `${o}px` : o), n.$$.dirty & /*value, gradio*/
    4608 && m.dispatch("change"), n.$$.dirty & /*value, rr*/
    12288 && a !== null && Array.isArray(a))
      for (const c of a)
        typeof c != "string" ? c.url && C.open(c.url) : C.open(c);
  }, [
    o,
    l,
    i,
    s,
    r,
    f,
    u,
    _,
    k,
    m,
    y,
    p,
    a,
    C,
    L,
    d
  ];
}
class Bn extends yn {
  constructor(e) {
    super(), Nn(this, e, Pn, Zn, An, {
      elem_id: 1,
      elem_classes: 2,
      visible: 3,
      height: 0,
      value: 12,
      container: 4,
      scale: 5,
      min_width: 6,
      loading_status: 7,
      interactive: 8,
      gradio: 9
    });
  }
  get elem_id() {
    return this.$$.ctx[1];
  }
  set elem_id(e) {
    this.$$set({ elem_id: e }), Z();
  }
  get elem_classes() {
    return this.$$.ctx[2];
  }
  set elem_classes(e) {
    this.$$set({ elem_classes: e }), Z();
  }
  get visible() {
    return this.$$.ctx[3];
  }
  set visible(e) {
    this.$$set({ visible: e }), Z();
  }
  get height() {
    return this.$$.ctx[0];
  }
  set height(e) {
    this.$$set({ height: e }), Z();
  }
  get value() {
    return this.$$.ctx[12];
  }
  set value(e) {
    this.$$set({ value: e }), Z();
  }
  get container() {
    return this.$$.ctx[4];
  }
  set container(e) {
    this.$$set({ container: e }), Z();
  }
  get scale() {
    return this.$$.ctx[5];
  }
  set scale(e) {
    this.$$set({ scale: e }), Z();
  }
  get min_width() {
    return this.$$.ctx[6];
  }
  set min_width(e) {
    this.$$set({ min_width: e }), Z();
  }
  get loading_status() {
    return this.$$.ctx[7];
  }
  set loading_status(e) {
    this.$$set({ loading_status: e }), Z();
  }
  get interactive() {
    return this.$$.ctx[8];
  }
  set interactive(e) {
    this.$$set({ interactive: e }), Z();
  }
  get gradio() {
    return this.$$.ctx[9];
  }
  set gradio(e) {
    this.$$set({ gradio: e }), Z();
  }
}
export {
  Wn as BaseExample,
  Bn as default
};
