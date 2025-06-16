# Components

## Core Components
The Courses project contains the following main components:

1. **PyTorch Implementation Examples**: 
   - Basic and advanced examples of machine learning models
   - Neural network implementations for different use cases

2. **Neo4j Examples**:
   - Cypher query examples
   - Graph database schemas and relationships

3. **Rust Programming Examples**:
   - Specific Rust implementations
   - Standard library usage examples

## Component Relationships
Each technology section is independent and serves as a separate learning module. There are no direct dependencies between the PyTorch, Neo4j, and Rust components.

## Module Structure
- Each technology has its own directory
- PyTorch examples are further organized into chapters based on complexity and topic
- Each component contains implementation files and documentation

## Key Classes/Functions

### PyTorch
- Linear regression and classification models
- CNN implementations for CIFAR dataset
- Sequence models for time series prediction

### Neo4j
- Cypher queries for crime and family graph examples

### Rust
- Card deck implementation

## Implementation Details

### PyTorch Sequence Models
The `sequence.ipynb` notebook in the `chapter_2_sequences` directory demonstrates:
- Creating synthetic time series data (sine waves with noise)
- Implementing a linear model for sequence prediction
- Training using PyTorch's optimization tools
- Two approaches for generating predictions:
  1. One-step forecasting using test data
  2. Multi-step forecasting with recursive prediction (where each prediction feeds into the next input)

## Data Models
- Time series data for sequence models
- Graph data for Neo4j examples
- Card deck model for Rust implementation
