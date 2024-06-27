import Image from "next/image";

export const fetchData = async () => {
  try {
    const res = await fetch("http://server:8000");
    return res.json();
  } catch (err) {
    return err;
  }
};

export default async function Home() {
  console.log(await fetchData());
  return (
    <main className="min-h-screen">
      <div className="">Content</div>
    </main>
  );
}
