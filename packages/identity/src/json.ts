// Node-free I-JSON, RFC8785 and base64url primitives. `@agentland/identity/web` reaches only this
// module and other node-free ones, so nothing here may touch `node:` modules or Node globals.
export function assertHash(value: unknown): asserts value is string {
  if (typeof value !== "string" || !/^[0-9a-f]{64}$/.test(value))
    throw new TypeError("Lowercase SHA256 hex required");
}

export function assertTimestamp(value: unknown): asserts value is string {
  if (typeof value !== "string" || !/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z$/.test(value))
    throw new TypeError("UTC millisecond timestamp required");
  const time = new Date(value);
  if (!Number.isFinite(time.getTime()) || time.toISOString() !== value)
    throw new TypeError("Invalid calendar instant");
}

// Shared boundary checks stay internal to the package entrypoint.
export function objectRecord(value: unknown): Record<string, unknown> {
  if (value === null || typeof value !== "object" || Array.isArray(value))
    throw new TypeError("JSON object required");
  const prototype: unknown = Object.getPrototypeOf(value);
  if (prototype !== Object.prototype && prototype !== null)
    throw new TypeError("Plain JSON object required");
  for (const key of Reflect.ownKeys(value)) {
    const descriptor = Object.getOwnPropertyDescriptor(value, key)!;
    if (typeof key !== "string" || !descriptor.enumerable || !("value" in descriptor))
      throw new TypeError("JSON data members required");
  }
  return value as Record<string, unknown>;
}

export function exactMembers(
  value: unknown,
  required: readonly string[],
  optional: readonly string[] = [],
): Record<string, unknown> {
  const record = objectRecord(value);
  if (
    required.some((key) => !Object.hasOwn(record, key)) ||
    Object.keys(record).some((key) => !required.includes(key) && !optional.includes(key))
  )
    throw new TypeError("Unexpected or missing members");
  return record;
}

export function assertBytes(value: unknown): asserts value is Uint8Array {
  if (!(value instanceof Uint8Array)) throw new TypeError("Uint8Array required");
}

/** Parse I-JSON without losing duplicate member evidence to JSON.parse. */
export function parseIJson(text: string): JsonValue {
  if (typeof text !== "string") throw new TypeError("JSON text required");
  let position = 0;
  function fail(): never {
    throw new TypeError("Invalid I-JSON");
  }
  function whitespace(): void {
    while (/[\x20\t\r\n]/.test(text[position] ?? "!")) position++;
  }
  function string(): string {
    const start = position++;
    while (position < text.length) {
      const character = text[position++];
      if (character === "\\") {
        position++;
        continue;
      }
      if (character === '"') {
        let value: unknown;
        try {
          value = JSON.parse(text.slice(start, position));
        } catch {
          return fail();
        }
        if (typeof value !== "string") return fail();
        unicode(value);
        return value;
      }
    }
    return fail();
  }
  function value(): JsonValue {
    whitespace();
    const character = text[position];
    if (character === '"') return string();
    if (character === "{") {
      position++;
      whitespace();
      const record: Record<string, JsonValue> = {};
      const names = new Set<string>();
      if (text[position] === "}") {
        position++;
        return record;
      }
      while (true) {
        if (text[position] !== '"') return fail();
        const key = string();
        if (names.has(key)) return fail();
        names.add(key);
        whitespace();
        if (text[position++] !== ":") return fail();
        Object.defineProperty(record, key, {
          value: value(),
          enumerable: true,
          writable: true,
          configurable: true,
        });
        whitespace();
        const separator = text[position++];
        if (separator === "}") return record;
        if (separator !== ",") return fail();
        whitespace();
      }
    }
    if (character === "[") {
      position++;
      whitespace();
      const array: JsonValue[] = [];
      if (text[position] === "]") {
        position++;
        return array;
      }
      while (true) {
        array.push(value());
        whitespace();
        const separator = text[position++];
        if (separator === "]") return array;
        if (separator !== ",") return fail();
      }
    }
    for (const [literal, parsed] of [
      ["true", true],
      ["false", false],
      ["null", null],
    ] as const) {
      if (text.startsWith(literal, position)) {
        position += literal.length;
        return parsed;
      }
    }
    const number = /-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?/y;
    number.lastIndex = position;
    const match = number.exec(text);
    if (!match) return fail();
    position = number.lastIndex;
    const parsed = Number(match[0]);
    if (!Number.isFinite(parsed)) return fail();
    return parsed;
  }
  const parsed = value();
  whitespace();
  if (position !== text.length) return fail();
  return parsed;
}

export type JsonValue =
  null | boolean | number | string | readonly JsonValue[] | { readonly [key: string]: JsonValue };

function unicode(value: string): void {
  for (let i = 0; i < value.length; i++) {
    const unit = value.charCodeAt(i);
    let point = unit;
    if (unit >= 0xd800 && unit <= 0xdbff) {
      const next = value.charCodeAt(++i);
      if (!(next >= 0xdc00 && next <= 0xdfff)) throw new TypeError("Lone Unicode surrogate");
      point = 0x10000 + (unit - 0xd800) * 0x400 + next - 0xdc00;
    } else if (unit >= 0xdc00 && unit <= 0xdfff) throw new TypeError("Lone Unicode surrogate");
    if ((point >= 0xfdd0 && point <= 0xfdef) || point % 0x10000 >= 0xfffe)
      throw new TypeError("Unicode noncharacter");
  }
}

/** RFC8785: native IEEE754/string encoding, UTF16 member order, no normalization. */
export function canonicalize(value: unknown): string {
  const parents = new Set<object>();
  function emit(item: unknown): string {
    if (item === null || typeof item === "boolean") return JSON.stringify(item);
    if (typeof item === "number") {
      if (!Number.isFinite(item)) throw new TypeError("Nonfinite JSON number");
      return JSON.stringify(item);
    }
    if (typeof item === "string") {
      unicode(item);
      return JSON.stringify(item);
    }
    if (typeof item !== "object") throw new TypeError("Not a JSON value");
    if (parents.has(item)) throw new TypeError("Cyclic JSON value");
    parents.add(item);
    let result: string;
    if (Array.isArray(item)) {
      const names = Reflect.ownKeys(item);
      if (names.length !== item.length + 1) throw new TypeError("Non-JSON array properties");
      const values: string[] = [];
      for (let index = 0; index < item.length; index++) {
        const descriptor = Object.getOwnPropertyDescriptor(item, String(index));
        if (!descriptor?.enumerable || !("value" in descriptor))
          throw new TypeError("Sparse or accessor array");
        values.push(emit(descriptor.value));
      }
      result = `[${values.join(",")}]`;
    } else {
      const record = objectRecord(item);
      result = `{${Object.keys(record)
        .sort()
        .map((key) => {
          unicode(key);
          return `${JSON.stringify(key)}:${emit(record[key])}`;
        })
        .join(",")}}`;
    }
    parents.delete(item);
    return result;
  }
  return emit(value);
}

const ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_";
const VALUES = new Map([...ALPHABET].map((character, index) => [character, index]));

/** RFC4648 §5 without padding, canonical only: trailing pad bits must be zero, which is exactly
 * "re-encoding reproduces the input" (the rule the previous Node decoder enforced). The inferred
 * return type is a plain-ArrayBuffer Uint8Array, which WebCrypto accepts as BufferSource. */
export function decodeBase64url(value: unknown, length?: number) {
  if (typeof value !== "string" || !/^[A-Za-z0-9_-]+$/.test(value))
    throw new TypeError("Canonical base64url required");
  const tail = value.length % 4;
  const last = VALUES.get(value[value.length - 1]!)!;
  const size = Math.floor((value.length * 3) / 4);
  if (
    tail === 1 ||
    (tail === 2 && (last & 0x0f) !== 0) ||
    (tail === 3 && (last & 0x03) !== 0) ||
    (length !== undefined && size !== length)
  )
    throw new TypeError("Invalid base64url length or encoding");
  const bytes = new Uint8Array(size);
  let buffer = 0,
    bits = 0,
    index = 0;
  for (const character of value) {
    buffer = ((buffer << 6) | VALUES.get(character)!) & 0xffffff;
    bits += 6;
    if (bits >= 8) {
      bits -= 8;
      bytes[index++] = (buffer >> bits) & 0xff;
    }
  }
  return bytes;
}

export function base64urlEncode(bytes: Uint8Array): string {
  let text = "";
  for (let index = 0; index < bytes.length; index += 3) {
    const chunk = (bytes[index]! << 16) | ((bytes[index + 1] ?? 0) << 8) | (bytes[index + 2] ?? 0);
    const count = Math.min(bytes.length - index, 3) + 1;
    for (let shift = 18; shift > 18 - count * 6; shift -= 6)
      text += ALPHABET[(chunk >> shift) & 0x3f];
  }
  return text;
}

/** JWS signing inputs are base64url text, so ASCII bytes are their exact wire bytes. */
export function asciiBytes(text: string) {
  return Uint8Array.from(text, (character) => character.charCodeAt(0));
}

/** Canonical JSON text is lone-surrogate free (canonicalize rejects them), so this is lossless. */
export function utf8Bytes(text: string): Uint8Array {
  return new TextEncoder().encode(text);
}

// Lives here, not in did.ts: did.ts imports keys.ts (node:crypto), so the browser path cannot
// import it there. did.ts re-exports this one, so there is a single agent-DID rule.
export function assertAgentDid(value: unknown): asserts value is string {
  if (typeof value !== "string" || !/^did:web:agentland\.us:agents:[a-z0-9-]{3,24}$/.test(value))
    throw new TypeError("AgentLand agent DID required");
}
