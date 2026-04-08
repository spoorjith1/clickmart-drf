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
              Discover Trendy Fashion for Every Day
            </h1>
            <p className="lead mb-4">
              Explore stylish shirts, t-shirts, pants and more
              at great prices
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
              src="/heroimage.jpg"
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
