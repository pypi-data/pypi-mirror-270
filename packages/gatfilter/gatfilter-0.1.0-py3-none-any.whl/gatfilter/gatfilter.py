import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from scipy.spatial import ConvexHull
from matplotlib.path import Path
from collections import defaultdict
import nltk

def load_dataset(filepath):
    """Load a dataset from a CSV or TSV file."""
    if filepath.endswith('.csv'):
        return pd.read_csv(filepath)
    elif filepath.endswith('.tsv'):
        return pd.read_csv(filepath, delimiter='\t')
    else:
        raise ValueError("Unsupported file format. Please provide a CSV or TSV file.")

def tokenize_text(dataframe, text_column):
    """Tokenize text in the specified column of a dataframe."""
    return dataframe[text_column].apply(nltk.word_tokenize)

def get_augment_method(augmented_path):
    """Determine the augmentation method based on the file path."""
    if "backtranslation" in augmented_path:
        return "BT"
    elif "EDA" in augmented_path:
        return "EDA"
    else:
        return "CA"

def plot_words(baseline_word_vectors, augmented_word_vectors, hull_path, label, augment_method, save_fig, save_dir):
    """Plot baseline and augmented word vectors with convex hull, and optionally save the figure."""
    plt.figure(figsize=(10, 10))
    plt.plot(hull_path[:, 0], hull_path[:, 1], lw=0.5, label='Convex Hull')
    plt.scatter(baseline_word_vectors[:, 0], baseline_word_vectors[:, 1], s=5, c='blue', label='Baseline Words')
    plt.scatter(augmented_word_vectors[:, 0], augmented_word_vectors[:, 1], s=5, c='red', label='Augmented Words')
    plt.title(f'2D Convex Hull for Label {label}')
    plt.xlabel('PCA Component 1')
    plt.ylabel('PCA Component 2')
    plt.legend()
    if save_fig:
        label_save_path = os.path.join(save_dir, f'{augment_method}_{label}.png')
        plt.savefig(label_save_path, bbox_inches='tight')
    plt.close()

def filter_augment(word_model, data_path, augmented_path, output_file_name, plot=False, save_fig=False, save_dir=None):
    """Process and analyze text data for augmentation effects, with optional plotting."""
    base_df = load_dataset(data_path)
    augmented_df = load_dataset(augmented_path)

    augment_method = get_augment_method(augmented_path)
    words = word_model.get_words()
    X = np.array([word_model.get_word_vector(word) for word in words])
    pca = PCA(n_components=2)
    X_reduced = pca.fit_transform(X)

    base_df['tokenized_text'] = tokenize_text(base_df, base_df.columns[0])
    augmented_df['tokenized_text'] = tokenize_text(augmented_df, augmented_df.columns[0])

    label_to_baseline_words = defaultdict(list)
    augmented_words_outside_hull_by_label = defaultdict(set)

    for _, row in base_df.iterrows():
        text_tokens, label = row['tokenized_text'], row[base_df.columns[1]]
        for word in text_tokens:
            if word in word_model:
                label_to_baseline_words[label].append(word)

    for label, baseline_words in label_to_baseline_words.items():
        baseline_word_vectors = np.array([X_reduced[words.index(word)] for word in baseline_words if word in words])
        augmented_texts = augmented_df[augmented_df.iloc[:, 1] == label]['tokenized_text']
        augmented_word_vectors = np.array([X_reduced[words.index(word)] for text in augmented_texts for word in text if word in words])

        if len(baseline_word_vectors) > 2:
            hull = ConvexHull(baseline_word_vectors)
            hull_path = np.append(baseline_word_vectors[hull.vertices], [baseline_word_vectors[hull.vertices[0]]], axis=0)
            if plot:
                plot_words(baseline_word_vectors, augmented_word_vectors, hull_path, label, augment_method, save_fig, save_dir)

            for text in augmented_texts:
                for word in text:
                    if word in words:
                        word_vector = X_reduced[words.index(word)]
                        if not Path(hull_path).contains_point(word_vector):
                            augmented_words_outside_hull_by_label[label].add(word)

    words_outside_hull_df = pd.DataFrame([{'label': label, 'filter_word': ' '.join(words)} for label, words in augmented_words_outside_hull_by_label.items()])
    words_outside_hull_df.to_csv(output_file_name, index=False)

    return augmented_words_outside_hull_by_label
