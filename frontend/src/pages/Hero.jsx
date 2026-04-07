const Hero = () => {
  const scrollToProducts = () => {
    const productsSection = document.getElementById("products");
    if (productsSection) {
      productsSection.scrollIntoView({ behavior: "smooth" });
    }
  };

  return (
    <section className="hero-section py-5">
      <div className="container">
        <div className="row align-items-center">
          <div className="col-lg-6 fade-in">
            <h1 className="display-4 fw-bold mb-4">
              Discover Various Fruits, Vegetables and many More...
            </h1>
            <p className="lead mb-4">
              Find the fresh and natural food items at unbeatable prices.
              Quality guaranteed with fast, secure delivery.
            </p>
            <div className="d-flex gap-3">
              <button
                type="button"
                className="btn btn-primary btn-lg"
                onClick={scrollToProducts}
              >
                <i className="bi bi-bag-plus me-2"></i>
                Shop Now
              </button>
              <button type="button" className="btn btn-outline-light btn-lg">
                <i className="bi bi-play-circle me-2"></i>
                Learn More
              </button>
            </div>
          </div>
          <div className="col-lg-6 text-center">
            <img
              src="https://www.lalpathlabs.com/blog/wp-content/uploads/2019/01/Fruits-and-Vegetables.jpg"
              alt="hero-img-display"
              className="img-fluid rounded-3 shadow-lg"
              style={{ maxHeight: "400px", objectFit: "cover" }}
            />
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;
