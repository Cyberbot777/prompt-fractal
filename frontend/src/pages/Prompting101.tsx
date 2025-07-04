export default function Prompting101() {
  return (
    <>
      <div className="bg-gradient-to-r from-black to-zinc-900 bg-opacity-95 backdrop-blur-md text-gray-300 px-6 py-10 min-h-screen w-full font-sans leading-relaxed">
        <h1 className="text-3xl font-extrabold text-gray-100 tracking-tight mb-8">
          Prompting 101 – How & Why
        </h1>

        <nav className="mb-8">
          <h2 className="text-xl font-semibold text-gray-300 tracking-tight mb-3">
            Table of Contents
          </h2>
          <ul className="space-y-2 pl-1">
            <li>
              <a
                href="#what"
                className="inline-block text-base text-blue-400 hover:text-gray-300 hover:scale-105 transition-all duration-200 tracking-tight"
              >
                What Is Prompting?
              </a>
            </li>
            <li>
              <a
                href="#why"
                className="inline-block text-base text-blue-400 hover:text-gray-300 hover:scale-105 transition-all duration-200 tracking-tight"
              >
                Why It Matters
              </a>
            </li>
            <li>
              <a
                href="#history"
                className="inline-block text-base text-blue-400 hover:text-gray-300 hover:scale-105 transition-all duration-200 tracking-tight"
              >
                A Brief History of AI
              </a>
            </li>
            <li>
              <a
                href="#training"
                className="inline-block text-base text-blue-400 hover:text-gray-300 hover:scale-105 transition-all duration-200 tracking-tight"
              >
                Understanding AI Training
              </a>
            </li>
            <li>
              <a
                href="#understanding"
                className="inline-block text-base text-blue-400 hover:text-gray-300 hover:scale-105 transition-all duration-200 tracking-tight"
              >
                How AI Understands Prompts
              </a>
            </li>
            <li>
              <a
                href="#tips"
                className="inline-block text-base text-blue-400 hover:text-gray-300 hover:scale-105 transition-all duration-200 tracking-tight"
              >
                Tips for Better Prompts
              </a>
            </li>
            <li>
              <a
                href="#personality"
                className="inline-block text-base text-blue-400 hover:text-gray-300 hover:scale-105 transition-all duration-200 tracking-tight"
              >
                Shaping an AI’s “Personality”
              </a>
            </li>
            <li>
              <a
                href="#sandbox"
                className="inline-block text-base text-blue-400 hover:text-gray-300 hover:scale-105 transition-all duration-200 tracking-tight"
              >
                PromptPilot: Your Testing Ground
              </a>
            </li>
          </ul>
        </nav>

        <section id="what" className="mb-8">
          <h2 className="text-2xl font-bold text-gray-100 tracking-tight mb-3">
            What Is Prompting?
          </h2>

          <p className="text-gray-300 leading-relaxed">
            Prompting is the act of giving a language model instructions. Think
            of it like talking to a very smart assistant — but one that only
            understands <em>exactly</em> what you tell it.
          </p>

          <p className="text-gray-300 leading-relaxed mt-4">
            Whether you’re a developer, writer, coach, or just curious —
            prompting is how you communicate with AI, how you communicate with
            yourself and others,{" "}
            <strong>
              and how you train and program it to respond to you and others.
            </strong>
          </p>

          <p className="text-gray-300 leading-relaxed mt-4">
            A good prompt can guide an AI to write, explain, summarize,
            role-play, solve problems, or take on a persona. Prompting is both
            an art and a tool — and like any tool, the better you understand it,
            the more powerful it becomes.
          </p>
        </section>

        <section id="why" className="mb-8">
          <h2 className="text-2xl font-bold text-gray-100 tracking-tight mb-3">
            Why It Matters
          </h2>

          <p className="text-gray-300 leading-relaxed">
            Artificial intelligence is becoming part of how we write, learn,
            build, and communicate — whether we realize it or not. But most
            people still don’t know how to shape what it says or how it thinks.
            That’s where prompting comes in.
          </p>

          <p className="text-gray-300 leading-relaxed mt-4">
            Prompting isn’t just about getting better answers. It’s about
            gaining control over how AI responds — not just accepting whatever
            it gives you.
          </p>

          <ul className="list-disc list-inside mt-4 space-y-1 text-gray-300">
            <li>Teach the AI what role to play</li>
            <li>Guide it to write or speak in your tone</li>
            <li>Ask better questions — and get better answers</li>
            <li>Build tools, assistants, or agents that reflect your goals</li>
          </ul>

          <p className="text-gray-300 leading-relaxed mt-4">
            In fact, did you know that every mainstream AI — like Grok and
            ChatGPT — allows you to personalize and customize your chat?
          </p>
        </section>

        <section id="history" className="mb-8">
          <h2 className="text-2xl font-bold text-gray-100 tracking-tight mb-3">
            A Brief History of AI
          </h2>

          <p className="text-gray-300 leading-relaxed">
            AI isn’t new. The idea of machines that think has been around for
            decades — even centuries in science fiction. But the kind of AI we
            use today, like ChatGPT or Claude, comes from a long evolution of
            breakthroughs and innovation.
          </p>

          <ul className="space-y-4 mt-4 text-gray-300 leading-relaxed">
            <li>
              <span className="font-semibold text-gray-200">1950s–1970s:</span>{" "}
              The Birth of the Idea – Alan Turing asked: Can machines think?
              This sparked early rule-based systems. They weren’t flexible — but
              they laid the foundation.
            </li>
            <li>
              <span className="font-semibold text-gray-200">1980s–1990s:</span>{" "}
              Expert Systems – AI ran on hard-coded rules. These systems made
              decisions in narrow fields — but couldn’t adapt or learn like
              humans.
            </li>
            <li>
              <span className="font-semibold text-gray-200">2000s–2010s:</span>{" "}
              Machine Learning – Data took over. Algorithms began learning
              patterns from massive datasets instead of being manually
              programmed. This era gave rise to deep learning and neural
              networks.
            </li>
            <li>
              <span className="font-semibold text-gray-200">2018–2020:</span>{" "}
              The Transformer Revolution – New models like BERT (from Google)
              and GPT (from OpenAI) introduced the Transformer architecture —
              allowing AI to generate language with remarkable coherence.
            </li>
            <li>
              <span className="font-semibold text-gray-200">2020–Today:</span>{" "}
              The Era of Large Language Models – We entered the age of LLMs like
              ChatGPT, Claude, Grok, Gemini, and more.
            </li>
          </ul>

          <p className="text-gray-300 leading-relaxed mt-4">
            <span className="text-gray-100 font-medium">
              ChatGPT, Claude, Grok, Gemini — these are all LLMs.
            </span>
            <br />
            They are trained on massive amounts of text to generate human-like
            responses — not by thinking, but by predicting patterns in language.
          </p>

          <p className="text-gray-300 leading-relaxed mt-4">
            That’s where{" "}
            <span className="text-gray-100 font-medium italic">you</span> come
            in.
            <br />
            You don’t need to build a model from scratch.
            <br />
            You just need to know how to talk to it — how to{" "}
            <span className="text-gray-100 font-medium italic">prompt</span> it.
          </p>
        </section>

        <section id="training" className="mb-8">
          <h2 className="text-2xl font-bold text-gray-100 tracking-tight mb-3">
            Understanding AI Training: Models, Fine-Tuning, and Prompting
          </h2>

          <p className="text-gray-300 leading-relaxed">
            There are different ways to “train” an AI — and knowing the
            difference helps you understand where prompting fits in.
          </p>

          <ol className="list-decimal list-inside mt-4 space-y-2 text-gray-300 leading-relaxed">
            <li>
              <strong>Pretraining:</strong> Companies like OpenAI and Anthropic
              train LLMs on huge text datasets. This is called pretraining — it
              teaches the model the structure of language. This process is
              expensive and done at scale.
            </li>
            <li>
              <strong>Fine-Tuning:</strong> Some teams go further by retraining
              a model on a smaller dataset to specialize it. This is useful for
              business use cases but requires ML expertise and resources.
            </li>
            <li>
              <strong>Prompting:</strong> One of the most accessible,
              user-friendly, and effective ways to “train” an AI — not by
              programming it, but by giving it instructions in plain text.
            </li>
          </ol>

          <p className="text-gray-300 leading-relaxed mt-4">
            <strong>
              Prompting is not lesser than the other training methods.
            </strong>{" "}
            You could argue it’s the most important — because it’s how the AI
            forms a “personality” and learns to respond to you.
          </p>

          <p className="text-gray-300 leading-relaxed mt-4">
            Precise prompts = better results. It takes iteration and reflection.
            Prompting can be simple or incredibly sophisticated — that
            flexibility is what makes it so powerful.
          </p>
        </section>

        <section id="understanding" className="mb-8">
          <h2 className="text-2xl font-bold text-gray-100 tracking-tight mb-3">
            How AI Understands Prompts
          </h2>

          <p className="text-gray-300 leading-relaxed">
            AI doesn’t think. It predicts.
          </p>

          <p className="text-gray-300 leading-relaxed mt-4">
            An LLM like GPT or Claude reads your input and uses patterns from
            its training data to guess what comes next — one word at a time.
          </p>

          <p className="text-gray-300 leading-relaxed mt-4">
            <strong>Everything you type into an AI is a prompt.</strong> If you
            want general results, you can be casual. If you want specific
            behavior, you need to be specific.
          </p>

          <p className="text-gray-300 leading-relaxed mt-4">
            That’s what <strong>prompt engineering</strong> is: writing targeted
            instructions that shape how the AI responds.
          </p>

          <h3 className="text-xl font-semibold text-gray-100 tracking-tight mt-6 mb-3">
            Context Matters
          </h3>

          <p className="text-gray-300 leading-relaxed">
            The model reads your prompt like a conversation. Instructions, tone,
            and past messages all shape the response — so clarity counts.
          </p>

          <h3 className="text-xl font-semibold text-gray-100 tracking-tight mt-6 mb-3">
            Guide the Pattern
          </h3>

          <p className="text-gray-300 leading-relaxed">
            You can steer the AI using:
          </p>

          <ul className="list-disc list-inside mt-4 space-y-1 text-gray-300 leading-relaxed">
            <li>
              <strong>Roles:</strong> “You are a coach…”
            </li>
            <li>
              <strong>Format:</strong> “Answer in bullet points.”
            </li>
            <li>
              <strong>Tone:</strong> “Use warm, casual language.”
            </li>
            <li>
              <strong>Thinking:</strong> “Solve this step-by-step.”
            </li>
          </ul>

          <p className="text-gray-300 leading-relaxed mt-4">
            Prompting is the art of shaping the prediction flow — guiding the
            output without ever touching code.
          </p>
        </section>

        <section id="tips" className="mb-8">
          <h2 className="text-2xl font-bold text-gray-100 tracking-tight mb-3">
            Tips for Better Prompts
          </h2>

          <ul className="list-disc list-inside space-y-2 text-gray-300 leading-relaxed">
            <li>
              <strong>Be clear about the role:</strong> “You are a kind, honest
              coach.”
            </li>
            <li>
              <strong>Give it a goal:</strong> “Help me improve this sentence.”
            </li>
            <li>
              <strong>Set the tone:</strong> “Be casual but clear.”
            </li>
            <li>
              <strong>Ask for format:</strong> “Return in Markdown list format.”
            </li>
            <li>
              <strong>Think step-by-step:</strong> “Walk me through the logic.”
            </li>
            <li>
              <strong>Use examples:</strong> “Reply like this: ‘Thank you for
              reaching out…’”
            </li>
          </ul>

          <h3 className="text-xl font-semibold text-gray-100 tracking-tight mt-6 mb-3">
            Prompting Is a Process
          </h3>

          <p className="text-gray-300 leading-relaxed">
            Prompting isn’t a one-shot command — it’s a training loop.{" "}
            <strong>
              This is called the iterative loop of prompt training, which is the
              method that GPT builders use to refine agents.
            </strong>
          </p>

          <p className="text-gray-300 leading-relaxed mt-4">
            Here’s the process:
          </p>

          <ul className="list-disc list-inside mt-2 space-y-1 text-gray-300 leading-relaxed">
            <li>Start general</li>
            <li>Interact and observe</li>
            <li>Try to break the AI’s character</li>
            <li>Refine the prompt</li>
            <li>Retest and improve</li>
          </ul>

          <p className="text-gray-300 leading-relaxed mt-4">
            This is <strong>prompt training</strong> — even without code. You’re
            adjusting behavior through careful iteration.
          </p>
        </section>

        <section id="personality" className="mb-8">
          <h2 className="text-2xl font-bold text-gray-100 tracking-tight mb-3">
            Shaping an AI’s “Personality”
          </h2>

          <p className="text-gray-300 leading-relaxed">
            AI has no emotions — but it can take on a{" "}
            <strong>personality</strong> based on how you prompt it.
          </p>

          <p className="text-gray-300 leading-relaxed mt-4">
            With clear instructions, it can be:
          </p>

          <ul className="list-disc list-inside mt-2 space-y-1 text-gray-300 leading-relaxed">
            <li>Friendly or cold</li>
            <li>Playful or serious</li>
            <li>Formal or poetic</li>
          </ul>

          <h3 className="text-xl font-semibold text-gray-100 tracking-tight mt-6 mb-3">
            Use the System Instruction
          </h3>

          <p className="text-gray-300 leading-relaxed">
            This is where you define tone and role.
            <br />
            “You are a kind teacher who explains clearly.”
            <br />
            “You are a cryptic oracle who never gives direct answers.”
          </p>

          <h3 className="text-xl font-semibold text-gray-100 tracking-tight mt-6 mb-3">
            Treat It Like a Character Sheet
          </h3>

          <p className="text-gray-300 leading-relaxed">
            Prompting is like writing a role for the AI to play. The clearer the
            role, the more consistent the behavior.
          </p>

          <p className="text-gray-300 leading-relaxed mt-4">
            You’re not just prompting — you’re <strong>directing</strong>.
          </p>
        </section>

        <section id="sandbox" className="mb-16">
          <h2 className="text-2xl font-bold text-gray-100 tracking-tight mb-3">
            PromptPilot: Your Testing Ground
          </h2>

          <p className="text-gray-300 leading-relaxed">
            PromptPilot was built for exactly this process — structured prompt
            training.
          </p>

          <p className="text-gray-300 leading-relaxed mt-4">
            It solves a real problem:{" "}
            <strong>
              prompt training is usually scattered across tabs, apps, and
              devices.
            </strong>
          </p>

          <p className="text-gray-300 leading-relaxed mt-4">
            You write in one place, test in another, flip to your phone, copy
            into ChatGPT or Claude — and lose focus fast.
          </p>

          <h3 className="text-xl font-semibold text-gray-100 tracking-tight mt-6 mb-3">
            One Place. One Window. Total Focus.
          </h3>

          <ul className="list-disc list-inside mt-2 space-y-1 text-gray-300 leading-relaxed">
            <li>
              Write your prompt and system instruction, see the response right
              next to the input
            </li>
            <li>
              Choose your model — GPT for now, with plans to support Claude and
              Grok soon
            </li>
            <li>
              Ability to save your prompts and instructions to your device and
              upload, with plans to save locally in the future
            </li>
            <li>Refine, replay, and export</li>
          </ul>

          <p className="text-gray-300 leading-relaxed mt-4">
            It’s a <strong>prompt training sandbox</strong> — purpose-built for
            clarity, focus, and iteration.
          </p>

          <h3 className="text-xl font-semibold text-gray-100 tracking-tight mt-6 mb-3">
            Compare Models. Sharpen Prompts. Learn Faster.
          </h3>

          <p className="text-gray-300 leading-relaxed">
            PromptPilot will support multiple models in the future, so you can
            test the same prompt across different LLMs — like GPT, Claude, or
            Grok — and compare how they behave.
          </p>

          <ul className="list-disc list-inside mt-2 space-y-1 text-gray-300 leading-relaxed">
            <li>Sharper prompts</li>
            <li>Better understanding of model behavior</li>
            <li>More informed tool choices</li>
          </ul>

          <p className="text-gray-300 leading-relaxed mt-4 font-medium">
            The goal is to bring those finalized prompts into your custom GPTs,
            assistants, or apps — already tuned and tested.
          </p>
        </section>

        <section id="resources" className="mt-10">
          <h2 className="text-2xl font-bold text-gray-300 tracking-tight mb-3">
            Further Reading & Resources
          </h2>
          <ul className="space-y-2 pl-1">
            <li>
              <a
                href="https://platform.openai.com/docs/guides/prompt-engineering"
                target="_blank"
                rel="noopener noreferrer"
                className="inline-block text-base text-blue-400 hover:text-gray-300 hover:scale-105 transition-all duration-200 tracking-tight"
              >
                OpenAI – Prompt Engineering Guide
              </a>
            </li>
            <li>
              <a
                href="https://github.com/openai/openai-cookbook"
                target="_blank"
                rel="noopener noreferrer"
                className="inline-block text-base text-blue-400 hover:text-gray-300 hover:scale-105 transition-all duration-200 tracking-tight"
              >
                OpenAI Cookbook – Real-World Prompt Examples
              </a>
            </li>
            <li>
              <a
                href="https://docs.anthropic.com/claude/docs/prompting"
                target="_blank"
                rel="noopener noreferrer"
                className="inline-block text-base text-blue-400 hover:text-gray-300 hover:scale-105 transition-all duration-200 tracking-tight"
              >
                Anthropic – Claude Prompting Guide
              </a>
            </li>
            <li>
              <a
                href="https://huggingface.co/learn/nlp-course/chapter1/1"
                target="_blank"
                rel="noopener noreferrer"
                className="inline-block text-base text-blue-400 hover:text-gray-300 hover:scale-105 transition-all duration-200 tracking-tight"
              >
                Hugging Face – What Are LLMs?
              </a>
            </li>
            <li>
              <a
                href="https://chat.openai.com/gpts/editor"
                target="_blank"
                rel="noopener noreferrer"
                className="inline-block text-base text-blue-400 hover:text-gray-300 hover:scale-105 transition-all duration-200 tracking-tight"
              >
                ChatGPT – Custom GPT Builder
              </a>
            </li>
            <li>
              <a
                href="https://claude.ai/"
                target="_blank"
                rel="noopener noreferrer"
                className="inline-block text-base text-blue-400 hover:text-gray-300 hover:scale-105 transition-all duration-200 tracking-tight"
              >
                Claude – Try Claude (Anthropic)
              </a>
            </li>
            <li>
              <a
                href="https://x.ai/blog/introducing-grok"
                target="_blank"
                rel="noopener noreferrer"
                className="inline-block text-base text-blue-400 hover:text-gray-300 hover:scale-105 transition-all duration-200 tracking-tight"
              >
                xAI – Intro to Grok
              </a>
            </li>
          </ul>
        </section>
      </div>
      <button
        onClick={() => window.scrollTo({ top: 0, behavior: "smooth" })}
        className="fixed bottom-6 right-6 bg-white/5 text-gray-200 px-4 py-2 text-sm rounded-full backdrop-blur-md hover:brightness-125 hover:scale-105 transition-all duration-200 z-50"
      >
        ↑ Top
      </button>
    </>
  );
}
