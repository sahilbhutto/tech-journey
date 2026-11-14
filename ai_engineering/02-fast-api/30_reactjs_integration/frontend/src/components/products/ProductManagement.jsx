import { useEffect, useState } from "react";
import {
  LuPackage,
  LuPlus,
  LuRefreshCw,
  LuSearch,
  LuShoppingBag,
  LuLayers,
  LuTag,
  LuCircleDollarSign,
  LuBoxes,
  LuLoaderCircle,
  LuCheck,
  LuX,
} from "react-icons/lu";

import { productService } from "../../services/productService";

import "./ProductManagement.css";

const initialForm = {
  name: "",
  sku: "",
  description: "",
  price: "",
  stock: 0,
  category_id: "",
  is_active: true,
};

function getArray(data) {
  if (Array.isArray(data)) return data;

  if (Array.isArray(data?.items)) return data.items;
  if (Array.isArray(data?.data)) return data.data;
  if (Array.isArray(data?.results)) return data.results;

  return [];
}

const ProductManagement = () => {
  const [form, setForm] = useState(initialForm);

  const [categories, setCategories] = useState([]);
  const [products, setProducts] = useState([]);

  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);

  const [search, setSearch] = useState("");

  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  // Fetch categories and products
  async function fetchData() {
    setLoading(true);
    setError("");

    try {
      const [categoryData, productData] = await Promise.all([
        productService.getCategories(),
        productService.getProducts(),
      ]);

      setCategories(getArray(categoryData));
      setProducts(getArray(productData));
    } catch (err) {
      setError(err.message || "Something went wrong");
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    fetchData();
  }, []);

  // Handle input changes
  function handleChange(e) {
    const { name, value, type, checked } = e.target;

    setForm((prev) => ({
      ...prev,
      [name]: type === "checkbox" ? checked : value,
    }));
  }

  // Create product
  async function handleSubmit(e) {
    e.preventDefault();

    setError("");
    setSuccess("");

    if (!form.category_id) {
      setError("Please select a category.");
      return;
    }

    if (Number(form.price) < 0 || Number(form.stock) < 0) {
      setError("Price and stock cannot be negative.");
      return;
    }

    const productData = {
      name: form.name.trim(),
      sku: form.sku.trim(),
      description: form.description.trim() || null,
      price: Number(form.price).toFixed(2),
      stock: Number(form.stock),
      category_id: Number(form.category_id),
      is_active: form.is_active,
    };

    setSubmitting(true);

    try {
      await productService.createProduct(productData);

      setSuccess("Product created successfully!");

      setForm(initialForm);

      // Refresh product list
      const updatedProducts = await productService.getProducts();

      setProducts(getArray(updatedProducts));
    } catch (err) {
      setError(err.message || "Unable to create product.");
    } finally {
      setSubmitting(false);
    }
  }

  // Search products
  const filteredProducts = products.filter((product) =>
    [
      product.name,
      product.sku,
      product.category?.name,
    ]
      .filter(Boolean)
      .some((value) =>
        String(value).toLowerCase().includes(search.toLowerCase())
      )
  );

  const activeProducts = products.filter(
    (product) => product.is_active
  ).length;

  return (
    <main className="product-page">

      {/* Header */}
      <header className="product-header">
        <div>
          <div className="product-breadcrumb">
            Dashboard <span>/</span> Inventory <span>/</span> Products
          </div>

          <h1>Product Management</h1>

          <p>
            Manage your inventory, create products and organize
            your product catalog.
          </p>
        </div>

        <button
          className="refresh-btn"
          onClick={fetchData}
          disabled={loading}
        >
          <LuRefreshCw className={loading ? "spin" : ""} />
          Refresh
        </button>
      </header>

      {/* Statistics */}
      <section className="product-stats">

        <div className="stat-card">
          <div className="stat-icon purple">
            <LuPackage />
          </div>

          <div>
            <span>Total Products</span>
            <h3>{products.length}</h3>
          </div>
        </div>

        <div className="stat-card">
          <div className="stat-icon green">
            <LuCheck />
          </div>

          <div>
            <span>Active Products</span>
            <h3>{activeProducts}</h3>
          </div>
        </div>

        <div className="stat-card">
          <div className="stat-icon orange">
            <LuLayers />
          </div>

          <div>
            <span>Categories</span>
            <h3>{categories.length}</h3>
          </div>
        </div>

        <div className="stat-card">
          <div className="stat-icon blue">
            <LuShoppingBag />
          </div>

          <div>
            <span>Inactive Products</span>
            <h3>{products.length - activeProducts}</h3>
          </div>
        </div>

      </section>

      {/* Alerts */}
      {error && (
        <div className="alert alert-error">
          <LuX />
          {error}
          <button onClick={() => setError("")}>
            <LuX />
          </button>
        </div>
      )}

      {success && (
        <div className="alert alert-success">
          <LuCheck />
          {success}
          <button onClick={() => setSuccess("")}>
            <LuX />
          </button>
        </div>
      )}

      {/* Create Product */}
      <section className="product-panel">

        <div className="panel-heading">
          <div className="panel-title-icon">
            <LuPlus />
          </div>

          <div>
            <h2>Create New Product</h2>
            <p>Add a new product to your inventory.</p>
          </div>
        </div>

        <form onSubmit={handleSubmit}>

          <div className="form-grid">

            {/* Product Name */}
            <div className="form-group">
              <label htmlFor="name">
                Product Name <span>*</span>
              </label>

              <div className="input-wrapper">
                <LuPackage />

                <input
                  id="name"
                  name="name"
                  type="text"
                  placeholder="e.g. Wireless Headphones"
                  value={form.name}
                  onChange={handleChange}
                  maxLength={200}
                  required
                />
              </div>
            </div>

            {/* SKU */}
            <div className="form-group">
              <label htmlFor="sku">
                SKU <span>*</span>
              </label>

              <div className="input-wrapper">
                <LuTag />

                <input
                  id="sku"
                  name="sku"
                  type="text"
                  placeholder="e.g. ELEC-001"
                  value={form.sku}
                  onChange={handleChange}
                  maxLength={64}
                  required
                />
              </div>
            </div>

            {/* Category */}
            <div className="form-group">
              <label htmlFor="category_id">
                Category <span>*</span>
              </label>

              <div className="input-wrapper">
                <LuLayers />

                <select
                  id="category_id"
                  name="category_id"
                  value={form.category_id}
                  onChange={handleChange}
                  required
                >
                  <option value="">Select a category</option>

                  {categories.map((category) => (
                    <option
                      key={category.id}
                      value={category.id}
                    >
                      {category.name}
                    </option>
                  ))}
                </select>
              </div>
            </div>

            {/* Price */}
            <div className="form-group">
              <label htmlFor="price">
                Price <span>*</span>
              </label>

              <div className="input-wrapper">
                <LuCircleDollarSign />

                <input
                  id="price"
                  name="price"
                  type="number"
                  placeholder="0.00"
                  min="0"
                  step="0.01"
                  value={form.price}
                  onChange={handleChange}
                  required
                />
              </div>
            </div>

            {/* Stock */}
            <div className="form-group">
              <label htmlFor="stock">
                Stock Quantity <span>*</span>
              </label>

              <div className="input-wrapper">
                <LuBoxes />

                <input
                  id="stock"
                  name="stock"
                  type="number"
                  placeholder="0"
                  min="0"
                  step="1"
                  value={form.stock}
                  onChange={handleChange}
                  required
                />
              </div>
            </div>

            {/* Status */}
            <div className="form-group">
              <label>Product Status</label>

              <label className="status-toggle">
                <input
                  type="checkbox"
                  name="is_active"
                  checked={form.is_active}
                  onChange={handleChange}
                />

                <span className="toggle-slider"></span>

                <span>
                  {form.is_active ? "Active" : "Inactive"}
                </span>
              </label>
            </div>

            {/* Description */}
            <div className="form-group full-width">
              <label htmlFor="description">
                Product Description
              </label>

              <textarea
                id="description"
                name="description"
                rows="4"
                placeholder="Write a short description about this product..."
                value={form.description}
                onChange={handleChange}
              />
            </div>

          </div>

          <div className="form-footer">
            <p>
              <span>*</span> Required fields
            </p>

            <button
              type="submit"
              className="create-btn"
              disabled={submitting}
            >
              {submitting ? (
                <>
                  <LuLoaderCircle className="spin" />
                  Creating...
                </>
              ) : (
                <>
                  <LuPlus />
                  Create Product
                </>
              )}
            </button>
          </div>

        </form>
      </section>

      {/* Products Table */}
      <section className="product-panel table-panel">

        <div className="table-heading">
          <div>
            <h2>All Products</h2>
            <p>
              View and manage your product inventory.
            </p>
          </div>

          <div className="table-actions">
            <div className="search-box">
              <LuSearch />

              <input
                type="search"
                placeholder="Search products..."
                value={search}
                onChange={(e) => setSearch(e.target.value)}
              />
            </div>

            <span className="product-count">
              {filteredProducts.length} Products
            </span>
          </div>
        </div>

        <div className="table-container">

          <table className="products-table">

            <thead>
              <tr>
                <th>PRODUCT</th>
                <th>SKU</th>
                <th>CATEGORY</th>
                <th>PRICE</th>
                <th>STOCK</th>
                <th>STATUS</th>
              </tr>
            </thead>

            <tbody>

              {loading ? (
                <tr>
                  <td colSpan="6" className="table-message">
                    <LuLoaderCircle className="spin" />
                    Loading products...
                  </td>
                </tr>
              ) : filteredProducts.length === 0 ? (
                <tr>
                  <td colSpan="6" className="table-message">
                    <LuPackage />
                    No products found.
                  </td>
                </tr>
              ) : (
                filteredProducts.map((product) => (
                  <tr key={product.id}>

                    <td>
                      <div className="product-name-cell">
                        <div className="product-avatar">
                          <LuPackage />
                        </div>

                        <div>
                          <strong>{product.name}</strong>
                          <small>Product #{product.id}</small>
                        </div>
                      </div>
                    </td>

                    <td>
                      <span className="sku-badge">
                        {product.sku}
                      </span>
                    </td>

                    <td>
                      {product.category?.name ||
                        categories.find(
                          (c) => c.id === product.category_id
                        )?.name ||
                        `Category #${product.category_id}`}
                    </td>

                    <td className="price-cell">
                      Rs. {Number(product.price).toFixed(2)}
                    </td>

                    <td>
                      <span
                        className={
                          product.stock === 0
                            ? "stock-badge out-stock"
                            : product.stock <= 5
                              ? "stock-badge low-stock"
                              : "stock-badge"
                        }
                      >
                        {product.stock} units
                      </span>
                    </td>

                    <td>
                      <span
                        className={`status-badge ${
                          product.is_active
                            ? "active"
                            : "inactive"
                        }`}
                      >
                        <span></span>
                        {product.is_active ? "Active" : "Inactive"}
                      </span>
                    </td>

                  </tr>
                ))
              )}

            </tbody>

          </table>
        </div>

      </section>

    </main>
  );
}


export default ProductManagement
