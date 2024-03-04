// Home.jsx
import React from "react";
import ResponsiveAppBar from "../components/ResponsiveAppBar";
import { SimpleFooter } from "../components/SimpleFooter";
import ActionAreaCard from "../components/HomeCard";

function Home() {

  const carddata = [
    {
      "name": "Card 1",
      "description": "Description for Card 1",
      "image": "https://example.com/image1.jpg"
    },
    {
      "name": "Card 2",
      "description": "Description for Card 2",
      "image": "https://example.com/image2.jpg"
    },
    {
      "name": "Card 3",
      "description": "Description for Card 3",
      "image": "https://example.com/image3.jpg"
    },
    {
      "name": "Card 4",
      "description": "Description for Card 4",
      "image": "https://example.com/image4.jpg"
    },
    {
      "name": "Card 5",
      "description": "Description for Card 5",
      "image": "https://example.com/image5.jpg"
    }
  ]
  



  return (
    <div>
      <ResponsiveAppBar />

      {/* hero section start */}
      <section className="hero">
      <div className="p-5 text-center bg-cover flex items-center justify-center h-screen" style={{backgroundImage: "url('https://assets.nicepagecdn.com/d2cc3eaa/2180580/images/panoramic-view-roys-peak-new-zealand-with-low-4-min.jpg')" }}></div>
      </section>
      {/* hero section end */}

      {/* Provided Services */}
        <ActionAreaCard data={carddata}/>

      {/* Provided Services end */}

      <SimpleFooter />
    </div>
  );
}

export default Home;
