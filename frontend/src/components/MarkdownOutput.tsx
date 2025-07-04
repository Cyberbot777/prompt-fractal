import ReactMarkdown from "react-markdown";

type Props = {
  content: string;
};

export default function MarkdownOutput({ content }: Props) {
  return (
    <div className="text-left">
      <ReactMarkdown>{content}</ReactMarkdown>
    </div>
  );
}
