import { useRef, useState, useEffect } from "react";
import PageWrapper from "../components/PageWrapper";
import { motion } from "framer-motion";
import { Save, UploadIcon } from "lucide-react";
import MarkdownOutput from "../components/MarkdownOutput";

export default function Prompt() {
  // State //
  const [systemInstruction, setSystemInstruction] = useState("");
  const [showExportMenu, setShowExportMenu] = useState(false);
  const [model, setModel] = useState("gpt-3.5-turbo");
  const [messages, setMessages] = useState([
    { role: "assistant", content: "Responses will show here...", model },
  ]);

  // Effect //
  useEffect(() => {
    setMessages([
      { role: "assistant", content: "Responses will show here...", model },
    ]);
  }, [model]);

  // listen for outside clicks or escape key //
  useEffect(() => {
    const handleClickOutside = (e: MouseEvent) => {
      if (
        exportMenuRef.current &&
        !exportMenuRef.current.contains(e.target as Node)
      ) {
        setShowExportMenu(false);
      }
    };

    const handleEscape = (e: KeyboardEvent) => {
      if (e.key === "Escape") {
        setShowExportMenu(false);
      }
    };

    document.addEventListener("mousedown", handleClickOutside);
    document.addEventListener("keydown", handleEscape);

    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
      document.removeEventListener("keydown", handleEscape);
    };
  }, []);

  // Refs //
  const outputRef = useRef<HTMLDivElement>(null);
  const fileInputRef = useRef<HTMLInputElement | null>(null);
  const systemInputRef = useRef<HTMLTextAreaElement | null>(null);
  const exportMenuRef = useRef<HTMLDivElement | null>(null);

  // Handler //
  const handleImportClick = () => {
    if (fileInputRef.current) {
      fileInputRef.current.click();
    }
  };

  // Export session as .json (includes instruction, model, and messages) //
  const handleExportSessionAsJSON = () => {
    const session = {
      systemInstruction,
      model,
      messages,
      date: new Date().toISOString(),
    };

    const blob = new Blob([JSON.stringify(session, null, 2)], {
      type: "application/json",
    });

    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `prompt-session-${Date.now()}.json`;
    a.click();
    URL.revokeObjectURL(url);
  };

  // Export only the system instruction as .txt //
  const handleExportAsTXT = () => {
    const blob = new Blob([systemInstruction], { type: "text/plain" });

    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `prompt-instruction-${Date.now()}.txt`;
    a.click();
    URL.revokeObjectURL(url);
  };

  return (
    <PageWrapper>
      {/* Top Row: Prompt Lab + Icons */}
      <div className="relative mb-2 h-10 -mt-4">
        {/* Prompt Lab */}
        <h1 className="text-2xl font-bold text-gray-100 tracking-tight absolute left-0 top-0">
          Prompt Lab
        </h1>

        {/* Model Selection */}
        <div className="absolute right-[50%] translate-x-[135px] top-3 font-mono text-sm text-gray-300 space-x-4">
          <label>
            <input
              type="radio"
              name="model"
              value="gpt-3.5-turbo"
              checked={model === "gpt-3.5-turbo"}
              onChange={(e) => setModel(e.target.value)}
              className="mr-1"
            />
            GPT
          </label>
          <label>
            <input
              type="radio"
              name="model"
              value="claude-3-5-sonnet-20241022"
              checked={model === "claude-3-5-sonnet-20241022"}
              onChange={(e) => setModel(e.target.value)}
              className="mr-1"
            />
            Claude
          </label>
        </div>
      </div>

      {/* File export/save + upload buttons - Top Right */}
      <div className="absolute right-10 top-9 flex gap-4 pr-1">
        {/* Save dropdown trigger */}
        <button
          onClick={() => setShowExportMenu((prev) => !prev)}
          className="hover:text-green-400 transition"
          title="Export session"
        >
          <Save size={18} />
        </button>

        {/* Upload button */}
        <button
          onClick={handleImportClick}
          className="hover:text-blue-400 transition"
          title="Import session file"
        >
          <UploadIcon size={18} />
        </button>
      </div>

      {/* Export dropdown menu */}
      {showExportMenu && (
        <div
          ref={exportMenuRef}
          className="absolute right-10 top-16 bg-black border border-green-700 text-green-300 text-sm font-mono shadow-md z-50"
        >
          <button
            onClick={() => {
              handleExportSessionAsJSON();
              setShowExportMenu(false);
            }}
            className="block w-full text-left px-3 py-1 hover:bg-green-800"
          >
            Export as .json
          </button>
          <button
            onClick={() => {
              handleExportAsTXT();
              setShowExportMenu(false);
            }}
            className="block w-full text-left px-3 py-1 hover:bg-green-800"
          >
            Export as .txt
          </button>
        </div>
      )}

      {/* File input for uploading .txt, .json, or .md system instructions */}
      <input
        type="file"
        accept=".txt,.json,.md"
        ref={fileInputRef}
        onChange={(e) => {
          const file = e.target.files?.[0];
          if (!file) return;

          const extension = file.name.split(".").pop()?.toLowerCase();
          const reader = new FileReader();

          reader.onload = (event) => {
            const text = event.target?.result as string;

            let contentToSet = "";

            if (extension === "json") {
              try {
                const data = JSON.parse(text);
                if (
                  data?.systemInstruction &&
                  typeof data.systemInstruction === "string"
                ) {
                  contentToSet = data.systemInstruction;
                } else {
                  console.warn(
                    "No systemInstruction field found in JSON file."
                  );
                }
              } catch (err) {
                console.error("Failed to parse JSON file", err);
              }
            } else {
              // .txt and .md just use the raw text
              contentToSet = text;
            }

            setSystemInstruction(contentToSet);

            // Auto-expand textarea after setting
            requestAnimationFrame(() => {
              if (systemInputRef.current) {
                const el = systemInputRef.current;
                el.style.height = "auto";
                el.style.height = `${el.scrollHeight}px`;
              }
            });
          };

          reader.readAsText(file);
        }}
        className="hidden"
      />

      {/* Two-Panel Layout */}
      <div className="flex flex-col md:flex-row gap-6 h-[80vh]">
        {/* Left Panel: System Instruction Input */}
        <div className="w-full md:w-1/2 bg-black/60 border border-zinc-800 rounded-xl p-4 shadow-inner">
          <div className="font-mono text-green-400 space-y-6">
            <div>
              <div className="whitespace-nowrap font-mono">
                <span className="text-gray-500">user@prompt-lab</span>
                <span className="text-blue-400">:~$</span>
                <span className="text-green-300 ml-2">System Instruction:</span>
              </div>

              <motion.textarea
                ref={systemInputRef}
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.3 }}
                value={systemInstruction}
                onChange={(e) => {
                  setSystemInstruction(e.target.value);
                  e.target.style.height = "auto";
                  e.target.style.height = `${e.target.scrollHeight}px`;
                }}
                placeholder="You are a helpful assistant..."
                className="w-full max-h-[70vh] overflow-auto bg-black border border-green-700 text-green-300 p-2 font-mono text-sm resize-none focus:outline-none focus:ring-2 focus:ring-green-400 custom-scroll"
              />
            </div>
          </div>
        </div>

        {/* Right Panel: GPT Chat Output */}
        <div className="w-full md:w-1/2 bg-zinc-900/40 border border-zinc-800 rounded-xl p-4 flex flex-col">
          <p className="text-blue-300 font-mono mb-2">Model Output</p>

          {/* Message Viewer */}
          <div
            ref={outputRef}
            className="flex-1 overflow-y-auto text-gray-300 font-mono text-sm space-y-2 scroll-output"
          >
            {messages.map((msg, i) => {
              if (
                i === 0 &&
                msg.role === "assistant" &&
                msg.content
                  .toLowerCase()
                  .includes("responses will show here") &&
                messages.length > 1
              ) {
                return null;
              }

              const label =
                msg.role === "user"
                  ? "You"
                  : msg.model?.includes("claude")
                  ? "Claude"
                  : "GPT";

              return (
                <div key={i}>
                  <span className="text-blue-400 font-bold mr-1">{label}:</span>
                  <MarkdownOutput content={msg.content} />
                </div>
              );
            })}
          </div>

          {/* User Input Field */}
          <div className="mt-4">
            <motion.textarea
              rows={1}
              placeholder="Type a message and press Enter..."
              onKeyDown={(e) => {
                if (e.key === "Enter" && !e.shiftKey) {
                  e.preventDefault();
                  const input = e.currentTarget.value.trim();
                  if (!input) return;

                  e.currentTarget.value = "";
                  e.currentTarget.style.height = "auto";

                  setMessages((prev) => [
                    ...prev,
                    {
                      role: "user",
                      content: input,
                      model,
                    },
                  ]);

                  console.log("VITE_API_URL:", import.meta.env.VITE_API_URL);
                  console.log("Sending to /api/generate:", {
                    systemInstruction,
                    messages: [...messages, { role: "user", content: input }],
                    model,
                  });

                  fetch(`${import.meta.env.VITE_API_URL}/api/generate`, {
                    method: "POST",
                    headers: {
                      "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                      systemInstruction,
                      messages: [...messages, { role: "user", content: input }],
                      model,
                    }),
                  })
                    .then((res) => res.json())
                    .then((data) => {
                      if (data.message) {
                        const fullReply = data.message;
                        let currentText = "";
                        let i = 0;

                        const typingInterval = setInterval(() => {
                          currentText += fullReply[i];
                          i++;

                          setMessages((prev) => {
                            const updated = [...prev];
                            if (
                              updated[updated.length - 1]?.role === "assistant"
                            ) {
                              updated.pop();
                            }
                            return [
                              ...updated,
                              {
                                role: "assistant",
                                content: currentText,
                                model,
                              },
                            ];
                          });

                          setTimeout(() => {
                            if (outputRef.current) {
                              outputRef.current.scrollTop =
                                outputRef.current.scrollHeight;
                            }
                          }, 0);

                          if (i >= fullReply.length) {
                            clearInterval(typingInterval);
                          }
                        }, 40);
                      } else {
                        setMessages((prev) => [
                          ...prev,
                          {
                            role: "assistant",
                            content: "Error: No response from model.",
                            model,
                          },
                        ]);
                      }
                    })
                    .catch((err) => {
                      setMessages((prev) => [
                        ...prev,
                        {
                          role: "assistant",
                          content: `Error: ${err.message}`,
                          model,
                        },
                      ]);
                    });
                }
              }}
              onInput={(e) => {
                e.currentTarget.style.height = "auto";
                e.currentTarget.style.height = `${e.currentTarget.scrollHeight}px`;
              }}
              className="w-full max-h-[200px] overflow-auto bg-zinc-900 border border-zinc-700 text-gray-100 p-2 font-mono text-sm resize-none focus:outline-none focus:ring-2 focus:ring-blue-400 rounded scroll-blue"
            />
          </div>
        </div>
      </div>
    </PageWrapper>
  );
}
